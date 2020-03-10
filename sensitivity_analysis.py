import pandas as pd
import numpy as np
from utils import retrieve_dataframe

def analysis():
	df = retrieve_dataframe()
	sensitivity_dict = {}
	for index, row in df.iterrows():
		mean_list = []
		sample_values = {}
		for i in df.itertuples():
			pairs = i[2]
			for i in pairs:
				sample_values.update({i: np.random.normal(i[0], abs(i[1]), 10000)})
		for i in range(0, 10000):
			sample_list = []
			for key, value in sample_values.items():
				sample_list.append(value[i])
			mean = (sum(sample_list)/len(sample_list))
			mean_list.append(mean)
		mean_array = np.array(mean_list)
		print(index)
		print(np.std(mean_array))
		sensitivity_dict.update({row['(processgrp, metric)']: np.std(mean_array)})
	print(sensitivity_dict)
	return sensitivity_dict

if __name__ == "__main__":
	analysis()
