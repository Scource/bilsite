from .models import tariff_data
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

		#works but need to change for sth more elegant
		for index, row in sheet.iterrows():
			date=pd.to_datetime(row['Data'], format='%Y-%m-%d')
			tariff_schemas=h
			del row['Data']
			hourly_data={'hour_1':row[1],
			'hour_2':row[2],
			'hour_3':row[3],
			'hour_4':row[4],
			'hour_5':row[5],
			'hour_6':row[6],
			'hour_7':row[7],
			'hour_8':row[8],
			'hour_9':row[9],
			'hour_10':row[10],
			'hour_11':row[11],
			'hour_12':row[12],
			'hour_13':row[13],
			'hour_14':row[14],
			'hour_15':row[15],
			'hour_16':row[16],
			'hour_17':row[17],
			'hour_18':row[18],
			'hour_19':row[19],
			'hour_20':row[20],
			'hour_21':row[21],
			'hour_22':row[22],
			'hour_23':row[23],
			'hour_24':row[24]}
			tariff_data.save_1h(hourly_data, date, tariff_schemas)

