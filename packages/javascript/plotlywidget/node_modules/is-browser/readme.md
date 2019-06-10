# is-browser

  Test whether you're running on the server or in the browser (using browserify)
## Installation

    $ npm install is-browser

## API

This simply exports `true` or `false`:

```javascript
if (require('is-browser')) {
  console.log('The module was installed using component');
} else {
  console.log('The module was installed using npm');
}
```

## License

MIT
