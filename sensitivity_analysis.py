import pandas as pd
import numpy as np
from process_metric_matching import import_csv

def analysis():
	#find all processes within processgrp, define processes[]
	# repeat 10000 times:
		#draw values from normal distribution of each process, processes[process] = samplevalue
		#calculate mean of samplevalues and store in listofmeans
	#calculate SD of listofmeans
	table = import_csv()
# 	print(table)
	
	

if __name__ == "__main__":
	analysis()
