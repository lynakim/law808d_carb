import pandas as pd
import numpy as np
#from utils import dataframe
from utils import retrieve_dataframe

def analysis():
	df = retrieve_dataframe()
	sensitivity_dict = {} #dictionary where key = (group, metric) and value = sensitivity
	for index, row in df.iterrows(): #calculates sensitivity for each row and adds it to sensitivity_dict
		mean_list = [] #list of means from each of the 10k iterations
		sample_values = {} #dictionary where key = (alpha, beta) and value = array of 10k samples from the distribution (alpha, beta)
		for i in row['Value-Std Pair']: #makes array of 10k samples for each process' (alpha, beta)
			sample_values.update({i: np.random.normal(i[0], i[1], 10000)})
		for i in range(0, 10000): #compiles 10k values from each (alpha, beta) to give 10k means
			sample_list = () #list of values from each (alpha, beta) for iteration i out of 10000
			for key, value in sample_values.items():
				sample_list.append(value[i])
			mean = (sum(sample_list)/len(sample_list) #mean for iteration i out of 10000
			mean_list.append(mean)
		sensitivity_dict.update({row['(Group, metric)']: np.std(mean_list)})
	print(sensitivity_dict)
	return sensitivity_dict

if __name__ == "__main__":
	analysis()
