from .models import tariff_data, zone_data, CSB_raw
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


def import_csb_data(file):
	xls_file=pd.ExcelFile(file)
	sheet=pd.read_excel(xls_file)

	sheets_to_del=['Lp.', 'Rodzaj_dokumentu', 'Typ_rozliczenia', 'Ilość']
	for d in sheets_to_del:
		del sheet[d]

	change_format=['Data_sprz', 'Data_od', 'Data_do']
	for c in change_format:
		sheet[c]=pd.to_datetime(sheet[c], format='%Y-%m-%d')

	lissss=[]
	for index, row in sheet.iterrows():
		a= CSB_raw(PPE_number=row['Nr_PPE'],
			SE_name=row['Sprzedawca'],
			SE_code=row['Kod_MDD'],
			tariff=row['Taryfa'],
			doc_numer=row['Numer_dokumentu'],
			sell_DT=row['Data_sprz'],
			invoice_DT_from=row['Data_od'],
			invoice_DT_to=row['Data_do'],
			zone_1=row['Strefa_1'],
			zone_2=row['Strefa_2'],
			zone_3=row['Strefa_3'])

		lissss.append(a)
	CSB_raw.save_data(lissss)

	



def CSB_decompose():

	# tarr_list =get distinct tarrifs from profiles
	tar_list=CSB_raw.objects.values_list('tariff').distinct()

	
	#Cget CSB data from model wehre flag=0
	CSBdata=CSB_raw.objects.filter(decomposed=0)
	CSBdf=pd.DataFrame.from_records(CSBdata)


	#get max and min date from CSBdata and get those from prof and zones + change on pandas
	dmin = CSBdata.order_by('invoice_DT_from').first().values('invoice_DT_from')
	dmax = CSBdata.order_by('invoice_DT_to').last().values('invoice_DT_to')

	prof_data=pd.DataFrame.from_records(tariff_data.objects.filter(tarrif_date__gte=dmin, tarrif_date__lte=dmax).order_by('tarrif_date'))
	zone_data=pd.DataFrame.from_records(zone_data.objects.filter(zone_date__gte=dmin, zone_date__lte=dmax).order_by('zone_date'))


	#for every in CSBlist:
	for index, row in CSBdf.iterrows():	

		if row['tariff'][0] in tar_list:

			# PPE_taryfa=row['tariff']
			# new_from=row['invoice_DT_from']
			# new_to=row['invoice_DT_to']
			# PPE_EC0=row['zone_1']
			# PPE_EC1=row['zone_2']

			temp_profiles=prof_data[(prof_data.tarrif_date >= row['invoice_DT_from']) & (prof_data.tarrif_date <=row['invoice_DT_to'])]
			temp_zones=zone_data[(zone_data.zone_date >= row['invoice_DT_from']) & (zone_data.zone_date <=row['invoice_DT_to'])]
			temp_profiles=temp_profiles['tarrif_schemas']=row['tariff']
			temp_zones=temp_zones['zone_schemas']=row['tariff']
			
			EC0_count_prof_h=0
			EC1_count_prof_h=0

			#temp_profiles.set_index('Data', inplace=True)
			#temp_zones.set_index('data', inplace=True)
			del temp_profiles['id']
			del temp_profiles['tariff_schemas']
			del temp_zones['id']
			del temp_zones['zone_schemas']


			zone_change=temp_zones.replace({0: 1, 1: 0})
			prof_change_0=temp_profiles.multiply(zone_change, fill_value=0)
			prof_change_1=temp_profiles.multiply(temp_zones, fill_value=0)

			prof_change_0_sum=(prof_change_0.sum()).sum()
			prof_change_1_sum=(prof_change_1.sum()).sum()


			temp_profiles_0=(prof_change_0*row['zone_1'])/prof_change_0_sum
			temp_profiles_1=(prof_change_1*row['zone_2'])/prof_change_1_sum
			temp_profiles = temp_profiles_0.add(temp_profiles_1, fill_value=0)

			temp_profiles['sum']=temp_profiles.sum(axis=1)

			for index, line in temp_profiles.iterrows():
				row['PPE_number']
				line['tariff_date'].month
				line['tariff_date'].year



																						#get from & to data + tariff for this invoice

																						#if tarr in tarr_list

																							#zones_change get 0->1, 1->0

																							#str=0 prof multiply by zones_changed
																							#str=1 prof multiply by zones normal

																							#sum str0 and str1

																							#str0*zone0 /sum str0     TABLE 
																							#str1*zone1 /sum str1     TABLE

																							#add tables

			#sum to days




		else:
			pass

			#get number of days in invoice period
			#sum all zones:
			#divide sum by number of days



		#check if PPE + month+year exists in tabkle
			#if true:
				#update object
			#else:
				#create objects and add

		#bulk create objects
