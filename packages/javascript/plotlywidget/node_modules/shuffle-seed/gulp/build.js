'use strict';

var gulp = require('gulp');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');

module.exports = function(options) {
	gulp.task('build', function() {
		return gulp.src('shuffle-seed.js')
		.pipe(uglify())
		.pipe(rename(function (path) {
			path.basename += ".min";
		}))
		.pipe(gulp.dest('./'));
	});
};
