# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

# urls:
# - http://stackoverflow.com/questions/3288595/multiprocessing-how-to-use-pool-map-on-a-function-defined-in-a-class
# - https://gist.github.com/kforeman/9d4e2b44bc5fc935d0fb#file-histogram-ipynb

import numpy as np
from multiprocessing import Pool


# create a pool
num_proc = 8
pool = Pool(processes=num_proc)
	
def parallel_histo():
	# simulate data
	size = 1e4
	data = np.random.normal(0, 5, size)

	# find min/max
	mn = data.min() - 1e-5
	mx = data.max() + 1e-5

	# find bins
	num_bins = 20
	bins = np.linspace(mn, mx, num_bins+1)

	# function to find bin counts for elements an array
	def find_bin_counts(x, bins=bins, array=data):
		# Note: you'll probably want some way of loading the data dynamically so it doesn't all have to be in memory
		binned = np.digitize(array[x[0]:x[1]], bins)
		return np.bincount(binned, minlength=num_bins+1)[1:] 
		# Note: not sure why there always seems to be an extra 0 at the front - seems to be built in to bincount to always count the number of zeros (of which we have none)	

	# partition data
	def partition(data, l):
	  for i in range(0, len(data), l):
		yield [i,i+l]
	partitions = list(partition(data, int(len(data)/num_proc)))
	
	# wrap the whole thing up in a function
	def fast_hist(data, partitions, bins):
		# first map
		mapped = pool.map(find_bin_counts, partitions)
		# then reduce
		reduced = np.vstack(mapped).sum(axis=0)
		return reduced

	# check to make sure map/reduce gets the same result as numpy's built in histogram
	result1 = fast_hist(data, partitions, bins)
	result2 = np.histogram(data, bins=bins)
	print(np.array_equal(result1, result2[0]))

parallel_histo()
