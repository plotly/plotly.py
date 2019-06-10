var from = require('from2')

var factory = module.exports = function(opts, arr){
	if(arguments.length<=1){
		arr = opts
		opts = {}
	}
	var reduce = [].concat(arr)
	return from(opts, function(size, cb){
		if(reduce.length<=0) return cb(null, null)
		cb(null, reduce.shift())
	})	
}

factory.obj = function(arr){
	return factory({
		objectMode:true
	}, arr)
}
