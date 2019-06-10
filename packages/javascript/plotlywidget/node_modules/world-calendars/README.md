# world-calendars
Node module for converting between various calendars

This project takes [kbwood/calendars](https://github.com/kbwood/calendars) and transforms them from a jQuery plugin to a node module. Many thanks to Keith Wood and all of the contributors to the original project! We support all the calendars in that project plus the Chinese lunar calendar.

kbwood/calendars was originally pulled at version 2.0.2 in October 2016.

The initial implementation converts all built-in calendars and localizations, including the `plus` module, but not the `validation` or `picker` functionality. Also includes basic test functionality.

Typical usage for converting from one date system to another goes through Julian days:
```
var calendars = require('world-calendars');

var gregorian = calendars.instance();
var nepali = calendars.instance('nepali');

// gives nepali date 2073-07-15
var nepaliHalloween = nepali.fromJD(gregorian.newDate(2016, 10, 31).toJD());
```
