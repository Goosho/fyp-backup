import pandas as pd
import math
path = 'temp_data.csv'
dataset = pd.read_csv(path , usecols = [0,1,2,3,4,5,6,7,8,9])
for index,row in dataset.iterrows():
  if  math.isnan(dataset['NOx'][index]) == True:
    dataset['NOx'][index]= 0
  if  math.isnan(dataset['Location'][index]) == True:
    dataset['Location'][index]= 'Gulshan-e-Ravi'
dataset.to_csv(r'temp_data.csv', index = False)
