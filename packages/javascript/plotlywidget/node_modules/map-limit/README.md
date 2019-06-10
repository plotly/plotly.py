# map-limit [![Flattr this!](https://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=hughskennedy&url=http://github.com/hughsk/map-limit&title=map-limit&description=hughsk/map-limit%20on%20GitHub&language=en_GB&tags=flattr,github,javascript&category=software)[![experimental](http://hughsk.github.io/stability-badges/dist/experimental.svg)](http://github.com/hughsk/stability-badges) #

[async.mapLimit](https://github.com/caolan/async#maplimitarr-limit-iterator-callback)'s
functionality available as a standalone npm module.

I often find myself pulling in [async](http://github.com/caolan/async) for this
method alone, so in the spirit of breaking things into smaller pieces here's
that method as a single thing you can require.

## Usage ##

[![map-limit](https://nodei.co/npm/map-limit.png?mini=true)](https://nodei.co/npm/map-limit)

### `mapLimit(arr, limit, iterator, callback)` ###

The same as map only no more than "limit" iterators will be simultaneously
running at any time.

Note that the items are not processed in batches, so there is no guarantee
that the first "limit" iterator functions will complete before any others are
started.

#### Arguments ####

* **arr** - An array to iterate over.
* **limit** - The maximum number of iterators to run at any time.
* **iterator(item, callback)** - A function to apply to each item in the array. The iterator is passed a callback(err, transformed) which must be called once it has completed with an error (which can be null) and a transformed item.
* **callback(err, results)** - A callback which is called after all the iterator functions have finished, or an error has occurred. Results is an array of the transformed items from the original array.

## License ##

MIT. See [LICENSE.md](http://github.com/hughsk/map-limit/blob/master/LICENSE.md) for details.
