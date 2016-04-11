import os
import re

def get_latest():
	os.system('pip show plotly > pip_version.txt')
	with open('pip_version.txt', 'r') as file:
		output = [i for i in file][2]
	latest_version = re.findall(r'\s.*\n', output)[0][1:-1]
	return latest_version

def run_duration(f, **kwargs):
	import timeit
	start_time = timeit.default_timer()
	f(**kwargs)
	return (timeit.default_timer() - start_time)







