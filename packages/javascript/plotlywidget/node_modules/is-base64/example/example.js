var isBase64 = require('is-base64');

var string = 'iVBORw0KGgoAAAANSUhEUgAABQAAAALQAQMAAAD1s08VAAAAA1BMVEX/AAAZ4gk3AAAAh0lEQVR42u3BMQEAAADCoPVPbQlPoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4GsTfAAGc95RKAAAAAElFTkSuQmCC';
var stringWithMime = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABQAAAALQAQMAAAD1s08VAAAAA1BMVEX/AAAZ4gk3AAAAh0lEQVR42u3BMQEAAADCoPVPbQlPoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4GsTfAAGc95RKAAAAAElFTkSuQmCC';

console.log(isBase64(string)); // true
console.log(isBase64(stringWithMime)); // false
console.log(isBase64(stringWithMime, {mime: true})); // true
console.log(isBase64('1342234')); // false
console.log(isBase64('afQ$%rfew')); // false
console.log(isBase64('dfasdfr342')); // false
console.log(isBase64('uuLMhh==')); // true
console.log(isBase64('uuLMhh')); // false
console.log(isBase64('uuLMhh', {paddingRequired: false})); // true
console.log(isBase64('')); // true
console.log(isBase64('', {allowBlank: false})); // false
