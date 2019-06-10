module.exports = {
  // Comments at the top of the file
  '//^': [
    '/**\n block comment at the top\n */', 
    '// comment at the top'
  ],

  // Comments at the bottom of the file
  '//$': ['// comment at the bottom'],

  // Comment for a property is the value of `'// <prop>'`
  '// a': [
    // Comments above property `a`
    [
      '// comment for a',
      '// comment line 2 for a',
      '/* block comment */'
    ],
    ['// comment at right']
  ],

  // The real value
  a: 1
};