'use strict';

var t = require('tape')
var split = require('.');

t('should throw an error when arguments are invalid', t => {
    t.throws(() => split());
    t.end()
});

t('readme', t => {

    t.deepEqual(
        split('a."b.c".d.{.e.f.g.}.h', '.'),
        ['a', '"b.c"', 'd', '{.e.f.g.}', 'h']
    )

    t.deepEqual(
        split('a."b.c".d.{.e.f.g.}.h', '.', {ignore: '""'}),
        ['a', '"b.c"', 'd', '{', 'e', 'f', 'g', '}', 'h']
    )
    t.end()
})

t('should not split on escaped dots:', t => {
    t.deepEqual(split('a.b.c\\.d', '.'), ['a', 'b', 'c\\.d']);
    t.deepEqual(split('a.b.c\\.d.e', '.'), ['a', 'b', 'c\\.d', 'e']);
    t.end()
});

t('should keep escaping when followed by a backslash:', t => {
    t.deepEqual(split('a.b.c\\\\.d', '.'), ['a', 'b', 'c\\\\', 'd']);
    t.deepEqual(split('a.b.c\\\\d', '.'), ['a', 'b', 'c\\\\d']);
    t.end()
});

t('should split a string on dots by default:', t => {
    t.deepEqual(split('a.b.c', '.'), ['a', 'b', 'c']);
    t.end()
});

t('should respect double-quoted strings', t => {
    t.deepEqual(split('"b.c"', '.'), ['"b.c"']);
    t.deepEqual(split('a."b.c"', '.'), ['a', '"b.c"']);
    t.deepEqual(split('a".b.c"', '.'), ['a".b.c"']);
    t.deepEqual(split('a."b.c".d', '.'), ['a', '"b.c"', 'd']);
    t.deepEqual(split('a."b.c".d.".e.f.g.".h', '.'), ['a', '"b.c"', 'd', '".e.f.g."', 'h']);
    t.end()
});

t('should respect singlequoted strings', t => {
    t.deepEqual(split('\'b.c\'', '.'), ['\'b.c\'']);
    t.deepEqual(split('a.\'b.c\'', '.'), ['a', '\'b.c\'']);
    t.deepEqual(split('a.\'b.c\'.d', '.'), ['a', '\'b.c\'', 'd']);
    t.deepEqual(split('a.\'b.c\'.d.\'.e.f.g.\'.h', '.'), ['a', '\'b.c\'', 'd', '\'.e.f.g.\'', 'h']);
    t.end()
});

t('should respect strings in backticks', t => {
    t.deepEqual(split('`b.c`', '.'), ['`b.c`']);
    t.deepEqual(split('a.`b.c`', '.'), ['a', '`b.c`']);
    t.deepEqual(split('a.`b.c`.d', '.'), ['a', '`b.c`', 'd']);
    t.deepEqual(split('a.`b.c`.d.`.e.f.g.`.h', '.'), ['a', '`b.c`', 'd', '`.e.f.g.`', 'h']);
    t.end()
});

t('should respect strings in double smart-quotes: “”', t => {
    t.deepEqual(split('“b.c”', '.'), ['“b.c”']);
    t.deepEqual(split('a.“b.c”', '.'), ['a', '“b.c”']);
    t.deepEqual(split('a.“b.c”.d', '.'), ['a', '“b.c”', 'd']);
    t.deepEqual(split('a.“b.c”.d.“.e.f.g.”.h', '.'), ['a', '“b.c”', 'd', '“.e.f.g.”', 'h']);
    t.end()
});

t('should retain unclosed double quotes in the results', t => {
    t.deepEqual(split('a."b.c', '.'), ['a', '"b', 'c']);
    t.end()
});

t('should retain unclosed single quotes in the results', t => {
    t.deepEqual(split('brian\'s', '.'), ['brian\'s']);
    t.deepEqual(split('a.\'b.c', '.'), ['a', '\'b', 'c']);
    t.end()
});



t('should split on a custom separator', t => {
    t.deepEqual(split('a/b/c', '/'), ['a', 'b', 'c']);
    t.deepEqual(split('a,b,c', ','), ['a', 'b', 'c']);
    t.end()
});

t('should not split on an escaped custom separator:', t => {
    t.deepEqual(split('a/b/c\\/d', '/'), ['a', 'b', 'c\\/d']);
    t.end()
});

t('should disable quotes support', t => {
    t.deepEqual(split('a.\'b.c\'."d"', '.', {ignore: '"'}), ['a', '\'b', 'c\'', '"d"']);
    t.end()
});

t('should keep single quotes', t => {
    t.deepEqual(split('a.\'b.c\'."d"', '.', {ignore: '\''}), ['a', '\'b.c\'', '"d"']);
    t.end()
});

t('should keep double quotes', t => {
    t.deepEqual(split('a."b.c".d', '.', '"'), ['a', '"b.c"', 'd']);
    t.end()
});

t('should keep “” double quotes', t => {
    t.deepEqual(split('a.“b.c”.d', '.', '“”'), ['a', '“b.c”', 'd']);
    t.end()
});

t('should keep backticks', t => {
    t.deepEqual(split('a.`b.c`.d', '.', {ignore: '`'}), ['a', '`b.c`', 'd']);
    t.end()
});

t('should allow custom quotes object', t => {
    t.deepEqual(split('a.^b.c$', '.', {ignore: '^$'}), ['a', '^b.c$']);
    t.deepEqual(split('a.^b.c^', '.', {ignore: '^^'}), ['a', '^b.c^']);
    t.deepEqual(split('a.~b.c~', '.', {ignore: '~~'}), ['a', '~b.c~']);
    t.end()
});

t('should keep escape characters', t => {
    t.deepEqual(split('a.b\\.c', '.', {escape: true}), ['a', 'b\\.c']);
    t.end()
});

t.skip('should throw when brackets are unclosed', t => {
    t.throws(function() {
    }, /unclosed/);
    t.end()
});

t('should not split inside brackets', t => {
    t.deepEqual(split('a.(b.c).d', '.'), ['a', '(b.c)', 'd']);
    t.deepEqual(split('a.[(b.c)].d', '.'), ['a', '[(b.c)]', 'd']);
    t.deepEqual(split('a.[b.c].d', '.'), ['a', '[b.c]', 'd']);
    t.deepEqual(split('a.{b.c}.d', '.'), ['a', '{b.c}', 'd']);
    t.deepEqual(split('a.<b.c>.d', '.'), ['a', '<b.c>', 'd']);
    t.end()
});

t('should support nested brackets', t => {
    t.deepEqual(split('a.{b.{c}.d}.e', '.'), ['a', '{b.{c}.d}', 'e']);
    t.deepEqual(split('a.{b.{c.d}.e}.f', '.'), ['a', '{b.{c.d}.e}', 'f']);
    t.deepEqual(split('a.{[b.{{c.d}}.e]}.f', '.'), ['a', '{[b.{{c.d}}.e]}', 'f']);
    t.end()
});

t.skip('should support escaped brackets', t => {
    t.deepEqual(split('a.\\{b.{c.c}.d}.e', '.'), ['a', '{b', '{c.c}', 'd}', 'e']);
    t.deepEqual(split('a.{b.c}.\\{d.e}.f', '.'), ['a', '{b.c}', '{d', 'e}', 'f']);
    t.end()
});

t('should support quoted brackets', t => {
    t.deepEqual(split('a.{b.c}."{d.e}".f', '.'), ['a', '{b.c}', '"{d.e}"', 'f']);
    t.deepEqual(split('a.{b.c}.{"d.e"}.f', '.'), ['a', '{b.c}', '{"d.e"}', 'f']);
    t.end()
});

t('should ignore imbalanced brackets', t => {
    t.deepEqual(split('a.{b.c', '.'), ['a', '{b', 'c']);
    t.deepEqual(split('a.{a.{b.c}.d', '.'), ['a', '{a', '{b.c}', 'd']);
    t.end()
});

