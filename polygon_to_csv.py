import pandas as pd

read_file = pd.read_csv(r'C:\Users\Smiti\Downloads\2020_coordinates.txt', error_bad_lines=False)
read_file.to_csv (r'C:\Users\Smiti\Documents\2020_gis.csv', index=None)
