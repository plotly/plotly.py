# right-now [![stable](http://hughsk.github.io/stability-badges/dist/stable.svg)](http://github.com/hughsk/stability-badges) #

Get the quickest, most high-resolution timestamp possible in node or the
browser.

Instead of returning the date, `right-now` may use `performance.now`,
`Date.now`, `+new Date` or `process.hrtime` to get a timestamp suitable for
measuring intervals of time. Handy for both animation loops and precision
benchmarking.

It's pretty small but saves me writing this boilerplate every time :)

## Installation ##

``` bash
npm install right-now
```

## Usage ##

### `require('right-now')()` ###

Returns a timestamp. In node, this uses `process.hrtime`. In the browser,
support for the following is checked in this order:

* `performance.now()`
* `Date.now()`
* `+new Date`
