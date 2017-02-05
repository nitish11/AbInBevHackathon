import pandas as pd
import glob
import numpy as np 

csv_list = glob.glob('/home/neeraj/learn/ABInBev/git/AbInBevHackathon/merged_data/*.csv')

data = []
for csv_file in csv_list:
	df = pd.read_csv(csv_file)
	print df.columns
	df_clean = pd.DataFrame.dropna(df)
	times_did_not_predict = 104 - df_clean.shape[0]
	try:	
		wrong_brand_name = np.sum((df_clean['Brand name detected'] == df_clean['Brand']).values)
	except:
		wrong_brand_name = None
	wrong_price = np.sum((df_clean['Recommended Price'] == df_clean['Price']).values)
	brand = df_clean.iloc[1]['Brand']
	sku = df_clean.iloc[1]['SKU']
	data.append([brand,sku,times_did_not_predict,wrong_price,wrong_brand_name])

df = pd.DataFrame(data)
df.columns = ['Brand', 'SKU', 'times_did_not_predict', 'wrong_price', 'wrong_brand_name']
df.to_csv('Details.csv')
