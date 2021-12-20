import pandas as pd
df20 = pd.read_csv('2020_with_emissions.csv')
df19 = pd.read_csv('2019_emissions.csv')
df18 = pd.read_csv('2018_emissions.csv')
df17 = pd.read_csv('2017_emissions.csv')
df16 = pd.read_csv('2016_emissions.csv')
df15 = pd.read_csv('2015_emissions.csv')
county_dict={}

for index, row in df20.iterrows():
    name = row['UNIT_ID']
    if name in county_dict.keys():
        county_dict[name] += row['SumOfPM25F_Lb']
        county_dict[name] += row['SumOfPM25S_Lb']
    else:
        county_dict[name] = row['SumOfPM25F_Lb']
        county_dict[name] = row['SumOfPM25S_Lb']

for index, row in df19.iterrows():
    name = row['UNIT_ID']
    if name in county_dict.keys():
        county_dict[name] += row['SumOfPM25F_Lb']
        county_dict[name] += row['SumOfPM25S_Lb']
    else:
        county_dict[name] = row['SumOfPM25F_Lb']
        county_dict[name] = row['SumOfPM25S_Lb']

for index, row in df18.iterrows():
    name = row['UNIT_ID']
    if name in county_dict.keys():
        county_dict[name] += row['SumOfPM25F_Lb']
        county_dict[name] += row['SumOfPM25S_Lb']
    else:
        county_dict[name] = row['SumOfPM25F_Lb']
        county_dict[name] = row['SumOfPM25S_Lb']
        
for index, row in df17.iterrows():
    name = row['UNIT_ID']
    if name in county_dict.keys():
        county_dict[name] += row['SumOfPM25F_Lb']
        county_dict[name] += row['SumOfPM25S_Lb']
    else:
        county_dict[name] = row['SumOfPM25F_Lb']
        county_dict[name] = row['SumOfPM25S_Lb']

for index, row in df16.iterrows():
    name = row['UNIT_ID']
    if name in county_dict.keys():
        county_dict[name] += row['SumOfPM25F_Lb']
        county_dict[name] += row['SumOfPM25S_Lb']
    else:
        county_dict[name] = row['SumOfPM25F_Lb']
        county_dict[name] = row['SumOfPM25S_Lb']
        
for index, row in df15.iterrows():
    name = row['UNIT_ID']
    if name in county_dict.keys():
        county_dict[name] += row['SumOfPM25F_Lb']
        county_dict[name] += row['SumOfPM25S_Lb']
    else:
        county_dict[name] = row['SumOfPM25F_Lb']
        county_dict[name] = row['SumOfPM25S_Lb']

values = county_dict.values()
sumval = sum(values)
for key, value in county_dict.items():
    county_dict[key] = value/sumval

from heapq import nlargest

topcounties = nlargest(10, county_dict, key = county_dict.get)
print(county_dict)
print(topcounties)
        
