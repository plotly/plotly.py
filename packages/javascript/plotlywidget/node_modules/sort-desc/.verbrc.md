# {%= name %} {%= badge("fury") %}

> {%= description %}

## Install
{%= include("install-npm", {save: true}) %}

## Usage

```js
var sortDesc = require('{%= name %}');
console.log((['d', 'c', 'b', 'a']).sort(sortDesc));
//=> ['a', 'b', 'c', 'd']
```

## Author
{%= include("author") %}

## License
{%= copyright() %}
{%= license() %}

***

{%= include("footer") %}