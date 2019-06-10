'use strict';

var fs = require('fs');
var path = require('path');
var gulp = require('gulp');
var git = require('gulp-git');
var bump = require('gulp-bump');
var tag_version = require('gulp-tag-version');
var runSequence = require('run-sequence');
var argv = require('yargs').argv;


module.exports = function(options) {
	var packageSrc = './package.json';

	gulp.task('release',function(done){
		return runSequence('git:bump', 'git:commit_release','git:tag','git:push',function(){
			process.exit();
		});
	})

	gulp.task('git:tag', function () {
		return gulp.src(packageSrc)
		.pipe(tag_version({
			message: '[Release] %VERSION%'
		}));
	});

	gulp.task('git:push',function(done){
		return git.push('origin', 'master', {
			args: '--tags'
		},function(err){
			if(err) console.error(err);
			done();
		});
	})

	// gulp.task('git:add',['mysql-backup'], function () { //hook mysql scheme to trigger at git add
	gulp.task('git:add', function () {
		return gulp.src(packageSrc)
			.pipe(git.add({args: " -A"}));
	});

	gulp.task('git:commit_release', ['git:add'], function () {
		var pkg = JSON.parse(fs.readFileSync(path.join(__dirname,'../package.json')));
		return gulp.src('./')
			.pipe(git.commit('[Release] Version '+pkg.version));
	});

	gulp.task('git:commit', ['git:add'], function () {
		return gulp.src('./')
			.pipe(git.commit((argv.m && argv!==true  ?  argv.m : 'Minor changes :coffee:')));
	});

	gulp.task('p', function(){
		runSequence('git:commit','git:push',function(){
			process.exit();
		});
	});

	gulp.task('git:bump', function () {
		return gulp.src([packageSrc,'./bower.json'])
		.pipe(bump({
			version: options.version,
			type: (argv.major ? 'major' : (argv.minor ? 'minor' : 'patch'))
		}))
		.pipe(gulp.dest('./'));
	});
}
