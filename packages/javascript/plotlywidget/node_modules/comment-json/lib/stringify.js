'use strict';

module.exports = stringify;

/////////////////////////////////////////////////////////////////////////////////////////////////////////
// Modified from Douglas Crockford's JSON2: 
// https://github.com/douglascrockford/JSON-js
/////////////////////////////////////////////////////////////////////////////////////////////////////////

var OBJ_PROTO = Object.prototype;
var KEY_PREFIX = '// ';
var KEY_PREFIX_LENGTH = 3;

// Format integers to have at least two digits.
function format_int(n) {
  return n < 10 ? '0' + n : n;
}


var escapable = /[\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g;
// table of character substitutions
var meta = {
  '\b': '\\b',
  '\t': '\\t',
  '\n': '\\n',
  '\f': '\\f',
  '\r': '\\r',
  '"' : '\\"',
  '\\': '\\\\'
};

function escape (string) {
  escapable.lastIndex = 0;
  if (!escapable.test(string)) {
    return string;
  }

  return string.replace(escapable, function(a) {
    var c = meta[a];
    return typeof c === 'string' 
      ? c 
      : '\\u' + ('0000' + a.charCodeAt(0).toString(16)).slice(-4);
  });
}


function quote(string) {
  // Escape no control characters, no quote characters, 
  // and no backslash characters, 
  // then we can safely slap some quotes around it.
  return '"' + escape(string) + '"';
}


function is_array (subject) {
  return OBJ_PROTO.toString.apply(subject) === '[object Array]';
}


function is_object (subject) {
  return subject && typeof subject === 'object';
}


// @param {string} key
// @param {Object} holder
// @param {function()|Array} replacer
// @param {string} indent
// @param {string} gap
function str(key, holder, replacer, indent, gap) {
  var value = holder[key];

  // If the value has a toJSON method, call it to obtain a replacement value.
  if (is_object(value) && typeof value.toJSON === 'function') {
    value = value.toJSON(key);
  }

  // If we were called with a replacer function, then call the replacer to
  // obtain a replacement value.
  if (typeof replacer === 'function') {
    value = replacer.call(holder, key, value);
  }

  switch (typeof value) {
    case 'string':
      return quote(value);

    case 'number':
      // JSON numbers must be finite. Encode non-finite numbers as null.
      return isFinite(value) ? String(value) : 'null';

    case 'boolean':
    case 'null':

      // If the value is a boolean or null, convert it to a string. Note:
      // typeof null does not produce 'null'. The case is included here in
      // the remote chance that this gets fixed someday.
      return String(value);

    // If the type is 'object', we might be dealing with an object or an array or
    // null.
    case 'object':

      // Due to a specification blunder in ECMAScript, typeof null is 'object',
      // so watch out for that case.
      if (!value) {
        return 'null';
      }

      var deeper_gap = gap + indent;
      // Make an array to hold the partial results of stringifying this object value.
      var partial = [];
      var length;
      var i;

      if (is_array(value)) {
        // The value is an array. Stringify every element. Use null as a placeholder
        // for non-JSON values.
        length = value.length;
        for (i = 0; i < length; i += 1) {
          partial[i] = str(i, value, replacer, indent, deeper_gap) || 'null';
        }

        // Join all of the elements together, separated with commas, and wrap them in
        // brackets.
        return partial.length === 0 
          ? '[]' 
          : deeper_gap
            ? '[\n'
              + deeper_gap + partial.join(',\n' + deeper_gap) + '\n' 
              + gap + ']' 
            : '[' + partial.join(',') + ']';
      }

      // If the replacer is an array, use it to select the members to be stringified.
      var k; // key
      var v;

      if (replacer && is_array(replacer)) {
        length = replacer.length;
        for (i = 0; i < length; i += 1) {
          if (typeof replacer[i] === 'string') {
            k = rep[i];
            v = str(k, value, replacer, indent, deeper_gap);
            if (v) {
              partial.push(deeper_gap + quote(k) + (deeper_gap ? ': ' : ':') + v + ',\n');
            }
          }
        }

      } else {
        var comment;
        var push_prev = function (last) {
          if (!prev) {
            return;
          }

          var v = prev[0];
          if (!deeper_gap) {
            partial.push(v);
            return;
          }
          
          var top = join(prev, 1, '\n' + deeper_gap);
          var right = prev[2];
          if (top) {
            // ```js
            // {
            //   '// a': {
            //     pos: 'top',
            //     body: '// comments'
            //   },
            //   a: 1
            // }
            // ```
            // -> 
            // ```
            // {
            //   // comments
            //   a: 1
            // }
            // ```
            v = deeper_gap + top + '\n' + v;
          }

          if (!last) {
            v += ',';
          }

          if (right) {
            // ```js
            // {
            //   '// a': {
            //     pos: 'right',
            //     body: '// comments'
            //   },
            //   a: 1
            // }
            // ```
            // -> 
            // ```
            // {
            //   a: 1 // comments
            // }
            // ```
            v += ' ' + join_comments(right);
          }
          partial.push(v + (last ? '' : '\n'));
        }

        var prev;

        // Otherwise, iterate through all of the keys in the object.
        for (k in value) {
          if (OBJ_PROTO.hasOwnProperty.call(value, k) && !is_comment(k, value)) {
            v = str(k, value, replacer, indent, deeper_gap);
            if (v) {
              push_prev();
              prev = [deeper_gap + quote(k) + (deeper_gap ? ': ' : ':') + v];

              // Only apply comments when argument `space` is not empty.
              if (deeper_gap && (comment = value[KEY_PREFIX + k])) {
                prev = prev.concat(comment);
              }
            }
          }
        }
      }

      push_prev(true);

      // Join all of the member texts together, separated with commas,
      // and wrap them in braces.
      return partial.length === 0 
        ? '{}' 
        : deeper_gap
          ? '{\n' 
            + partial.join('').replace(/,\n$/, '') + '\n' 
            + gap + '}'
          : '{' + partial.join(',') + '}';
  }
}


function is_comment (key, holder) {
  return key === '//^'
    || key === '//$'
    || !!~key.indexOf(KEY_PREFIX)
      // And the corresponding property must exist
      && key.slice(KEY_PREFIX_LENGTH) in holder;
}


// @param {function()|Array} replacer
// @param {string|number} space
function stringify (value, replacer, space) {

  // The stringify method takes a value and an optional replacer, and an optional
  // space parameter, and returns a JSON text. The replacer can be a function
  // that can replace values, or an array of strings that will select the keys.
  // A default replacer method can be provided. Use of the space parameter can
  // produce text that is more easily readable.

  // If the space parameter is a number, make an indent string containing that
  // many spaces.
  var i;
  var indent = '';
  if (typeof space === 'number') {
    for (i = 0; i < space; i += 1) {
      indent += ' ';
    }

  // If the space parameter is a string, it will be used as the indent string.
  } else if (typeof space === 'string') {
    indent = space;
  }

  // If there is a replacer, it must be a function or an array.
  // Otherwise, throw an error.
  if (replacer && typeof replacer !== 'function' && !is_array(replacer)) {
    throw new Error('JSON.stringify');
  }

  if (!is_object(value)) {
    return str('', {'': value}, replacer, indent, '');
  }

  var head_comments = join(value, '//^');
  var foot_comments = join(value, '//$');

  var result = str('', {'': value}, replacer, indent, '');

  // Make a fake root object containing our value under the key of ''.
  // Return the result of stringifying the value.
  return indent
    ? [head_comments, result, foot_comments]
      // filter empty `head_comments` or `foot_comments`
      .filter(Boolean)
      .join('\n')
    : result;
};


function join (host, key, joiner) {
  return host[key]
    ? join_comments(host[key], joiner)
    : '';
}


function join_comments (value, joiner) {
  return is_array(value)
    ? value.join(joiner || '\n')
    : value;
}
