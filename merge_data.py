import pandas as pd 
import numpy as np 
import pickle
import os

def cleanup_prices(df):
	for i in xrange(df['Price'].shape[0]):
		# print df.iloc[i]
		if len(df['Price'][i].split(' ')) == 1 and len(df['Price'][i]):
			df['Price'] = df['Price'][:2] + ' ' + df['Price'][2:]
	print df.head() 

def merge_csv(df_given, df):
	
	# print df_given.head()
	print df.head()

	# print df_given.shape
	print df.shape

	df['Date'] = pd.to_datetime(df['Date'])
	df_new = pd.merge(df_given,df,on=['Date','Brand','SKU'])
	#df_new.to_csv('merged_data_with_contour.csv')

	return df_new

if __name__ == '__main__':
	df_given = pd.read_excel('/home/maverick/ipython-notebooks/hack/ABI_Price_List.xlsx')

	fileNames = os.listdir('/home/maverick/ipython-notebooks/hack/pickleFiles/')

	for fileName in fileNames:
		# df = pd.read_csv('/home/neeraj/learn/ABInBev/pytesser_v0.0.1/labels_csv_with_contour.csv')
		df = pickle.load(open('/home/maverick/ipython-notebooks/hack/pickleFiles/'+fileName))

		OCRlist = []

		for OCRstring in df['OCR_data']:
			OCRlist.append(OCRstring.encode('ascii', 'ignore').decode('ascii'))

		df['OCR_data'] = OCRlist

		brand = fileName.split('.')[0]

		brand_name = []
		price = []
		for i in xrange(len(df)):
			brand_name.extend([df.iloc[i]['OCR_data'].splitlines()[0]])
			print df.iloc[i]['OCR_data'].splitlines()
			if '$' not in df.iloc[i]['OCR_data'].splitlines()[-1]:
				price.extend([''])
			else: 
				price.extend([df.iloc[i]['OCR_data'].splitlines()[-1].split('$')[-1]])
			print price[-1]
			
		df['Brand name detected'] = pd.Series(brand_name)
		df['Price'] = pd.Series(price)
		
		df_new = merge_csv(df_given, df[['Date','Brand','SKU','Price','Brand name detected']])
		# print df_new.head()
		# cleanup_prices(df_new)
		df_new.to_csv('final/'+brand+'_merged_data_brand_and_price.csv')


