import pandas as pd
import numpy as np
import csv
from utils import retrieve_dataframe

def analysis():
	df = retrieve_dataframe()
	sensitivity_dict = {}
	for index, row in df.iterrows():
		mean_list = []
		sample_values = {}
		for i in row['(value, std) pairs']:
			sample_values.update({i: np.random.normal(i[0], abs(i[1]), 10000)})
		for k in range(0, 10000):
			sample_list = []
			for key, value in sample_values.items():
				sample_list.append(value[k])
			mean = (sum(sample_list)/len(sample_list))
			mean_list.append(mean)
		mean_array = np.array(mean_list)
		sensitivity_dict.update({row['(processgrp, metric)']: np.std(mean_array)})
	#the following lines of code save the dictionary of values to a csv file; if we just require the dictionary, comment these lines out
	csv_file = open("stdev_values.csv", "w")
	writer = csv.writer(csv_file)
	for key, value in sensitivity_dict.items():
		writer.writerow([key, value])
	csv_file.close()
	return sensitivity_dict

if __name__ == "__main__":
	analysis()
