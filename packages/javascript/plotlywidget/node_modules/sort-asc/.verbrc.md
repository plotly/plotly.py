# {%= name %} {%= badge("fury") %}

> {%= description %}

## Install
{%= include("install-npm", {save: true}) %}

## Usage

```js
var sortAsc = require('{%= name %}');
console.log((['a', 'b', 'c', 'd']).sort(sortAsc));
//=> ['d', 'c', 'b', 'a']
```

## Author
{%= include("author") %}

## License
{%= copyright() %}
{%= license() %}

***

{%= include("footer") %}