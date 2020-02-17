import pandas as pd
import numpy as np
from utils import import_csv

def analysis(processgrp, metric):
	#find all processes within processgrp, define processes[]
	# repeat 10000 times:
		#draw values from normal distribution of each process, processes[process] = samplevalue
		#calculate mean of samplevalues and store in listofmeans
	#calculate SD of listofmeans
	df = import_csv("quant_metrics.csv")
# 	print(df.head(5))
	processes = list(set(df["ProcessGroup"].values))
	
