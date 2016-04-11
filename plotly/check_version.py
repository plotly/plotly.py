import urllib2  # the lib that handles the url stuff
import re


def get_latest():
	data = urllib2.urlopen('https://raw.githubusercontent.com/plotly/plotly.py/master/plotly/version.py') # it's a file like object and works just like a file
	version_string = [i for i in data][0]
<<<<<<< HEAD
	latest_version = re.findall(r'\'.*\'', version_string)[0][1:-1]
=======
	latest_version = re.findall(r'\'.*', version_string)[0][1:-1]
>>>>>>> 293645169191f9e9451f689197c7526ab214268f
	return latest_version

def run_duration(f, **kwargs):
	import timeit
	start_time = timeit.default_timer()
	f(**kwargs)
	return (timeit.default_timer() - start_time)
<<<<<<< HEAD

=======
	
>>>>>>> 293645169191f9e9451f689197c7526ab214268f






