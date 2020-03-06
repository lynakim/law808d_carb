import pandas as pd
import numpy as np
#from utils import dataframe
from utils import retrieve_dataframe

def analysis():
	df = retrieve_dataframe()
	sensitivity_dict = {}
	for index, row in df.iterrows():
		mean_list = []
		sample_values = {}
		for i in row['Value-Std Pair']:
			sample_values.update({i: np.random.normal(i[0], i[1], 10000)})
		for i in range(0, 10000):
			sample_list = ()
			for key, value in sample_values.items():
				sample_list.append(value[i])
			mean = (sum(sample_list)/len(sample_list)
			mean_list.append(mean)
		sensitivity_dict.update({'row['Value-Std Pair']': np.std(mean_list)})
	return sensitivity_dict

if __name__ == "__main__":
	analysis()
