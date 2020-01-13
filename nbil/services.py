from .models import tariff_data, zone_data
import pandas as pd
import numpy as np


#tutaj classa do wycigania danych z xlsa i obrobienia na dane do modelu
def import_ELP(file):
	xls_file = pd.ExcelFile(file)
	for h in xls_file.sheet_names:
		if h == 'B11,B12' or h == 'B11, B12':
			continue
		sheet=pd.read_excel(xls_file, h)
		sheet['Data']=pd.to_datetime(sheet['Data'], format='%Y-%m-%d')
		del sheet['Dzień']		
		
		#get rid of hour 2a
		location_2a=sheet.loc[sheet['2a'].notnull() == True]
		date_2a=location_2a.iloc[0]['Data']
		date_index=np.where(sheet['Data']==date_2a)[0]
		value_2a=location_2a.iloc[0]['2a']
		sheet.ix[date_index, 3] += value_2a
		del sheet['2a']

		for index, row in sheet.iterrows():
			date=pd.to_datetime(row['Data'], format='%Y-%m-%d')
			tariff_schemas=h
			del row['Data']
			hourly_data={}
			for g in range (1,25):
				new={'hour_'+str(g):row[g]}
				hourly_data.update(new)
			tariff_data.save_file(hourly_data, date, tariff_schemas)


def import_ELZ(file):
	xls_file = pd.ExcelFile(file)
	for h in xls_file.sheet_names:
		if h == 'B11,B12' or h == 'B11, B12':
			continue
		sheet=pd.read_excel(xls_file, h)
		del sheet['dzień tygodnia 2']		

		for index, row in sheet.iterrows():
			date=pd.to_datetime(row['data'], format='%Y-%m-%d')
			zone_schemas=h
			del row['data']
			hourly_data={}
			for g in range (1,25):
				new={'hour_'+str(g):row[g]}
				hourly_data.update(new)
			zone_data.save_file(hourly_data, date, zone_schemas)