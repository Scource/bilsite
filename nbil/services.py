from .models import tariff_data, zone_data, CSB_raw, CSB_data, UR_objects, CSPR_data
import pandas as pd
import numpy as np
from django.db.models import Count, F, Value
import cx_Oracle
from datetime import datetime, date, timedelta


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


		if CSB_raw.objects.filter(PPE_number=row['Nr_PPE'], SE_code=row['Kod_MDD'], doc_numer=row['Numer_dokumentu'], sell_DT=row['Data_sprz']).exists():
			pass
		else:
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

	
def get_tariff_list():
	tars = [i[0] for i in CSB_raw.objects.values_list('tariff').distinct()]
	return tars

def get_min_max_dates(CSBdata):
	dmin = (CSBdata.order_by('invoice_DT_from').values('invoice_DT_from').first()).get('invoice_DT_from')
	dmax = (CSBdata.order_by('invoice_DT_to').values('invoice_DT_to').last()).get('invoice_DT_to')
	return dmin, dmax


def deco_low_tariff(prof_data, stref_data, row, index, user_data):
	#HERE
	EC0_count_prof_h=0
	EC1_count_prof_h=0
	
	temp_profiles_all=prof_data[(prof_data.tariff_date >= row['invoice_DT_from']) & (prof_data.tariff_date <=row['invoice_DT_to'])]
	temp_zones_all=stref_data[(stref_data.zone_date >= row['invoice_DT_from']) & (stref_data.zone_date <=row['invoice_DT_to'])]
	temp_profiles=temp_profiles_all[temp_profiles_all['tariff_schemas']==row['tariff']]
	temp_zones=temp_zones_all[temp_zones_all['zone_schemas']==row['tariff']]
			
	

	del temp_profiles['id']
	del temp_profiles['tariff_schemas']
	del temp_zones['id']
	del temp_zones['zone_schemas']

	temp_profiles.set_index('tariff_date', inplace=True)
	temp_zones.set_index('zone_date', inplace=True)

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
		SE=UR_objects.objects.get(code=row['SE_code'], is_pob=1)		
		year=index.year
		month=index.month
		ppe=row['PPE_number']

		fetched = CSB_data.objects.get_or_create(PPE_number=ppe, month_date=index.month, year_date=index.year, SE_name=SE, user_id=user_data)

		if fetched:
			object_data={'value_d'+str(index.day): F('value_d'+str(index.day))+line['sum'], 'tariff_d'+str(index.day):row['tariff'], 'SE_name':SE, 'user_id':user_data}					
			CSB_data.save_obj(ppe, year, month, object_data)
	

def CSB_decompose(user_data):

	#get list of all tarrifs in db table
	tar_list=get_tariff_list()
	
	#get CSB data from model wehre flag=0
	CSBdata=CSB_raw.objects.values().filter(decomposed=0)
	if CSBdata.count()>0:
		CSBdf=pd.DataFrame.from_records(CSBdata)

		edges = get_min_max_dates(CSBdata)

		prof_data=pd.DataFrame(tariff_data.objects.values().order_by('tariff_date').filter(tariff_date__gte=edges[0], tariff_date__lte=edges[1]))
		stref_data=pd.DataFrame(zone_data.objects.values().order_by('zone_date').filter(zone_date__gte=edges[0], zone_date__lte=edges[1]))

		for index, row in CSBdf.iterrows():	
			if row['tariff'] in tar_list:
				deco_low_tariff(prof_data, stref_data, row, index, user_data)

			else:
				pass
				# add handling somehow C2+B+A tariffs

		CSBdata.update(decomposed=1)


def fetch_cspr_data():
	conn=cx_Oracle.connect('tomwal/09ToWaTW54@10.6.5.222:1521/skome')
	result=pd.DataFrame(columns=['PPE', "MDD_code", 'year', 'month'])

	sdate = date(2017, 2, 1)
	edate = date(2017, 3, 2)
	delta = edate - sdate

	try:
		for i in (range(delta.days + 1)):
			d=sdate + timedelta(days=i)

			day_only=int(d.strftime('%d'))
		
			query="""SELECT FORMULA.I_MB_PPE AS "PPE", EXTRACT(month FROM ENERGY100_A.I_DATETIME) "month", EXTRACT(year FROM ENERGY100_A.I_DATETIME) "year",
				I_ENERGY_CADO as "ener{suff}", I_STATUS_CADO as "status{suff}", I_TARIFF_SCHEMA.I_NAME as "tariff{suff}", I_COMPANY.I_OR_CODE as "MDD_code"
				FROM ENERGY100_A 
				INNER JOIN FORMULA ON FORMULA.I_ECPP_FID=ENERGY100_A.I_FORMULA_ID
				inner join I_COMPANY ON I_COMPANY.I_COMPANY_ID=ENERGY100_A.I_SE_ID
				INNER JOIN I_TARIFF_SCHEMA ON I_TARIFF_SCHEMA.I_TARIFF_SCHEMA_ID=ENERGY100_A.I_TARIFF_SCHEMA_ID
				WHERE ENERGY100_A.I_DATETIME = TO_DATE('{day}','YYYY-MM-DD')
				AND I_SE_ID =8460""".format(day=d, suff='_'+str(day_only))
			
			cspr_df = pd.read_sql(query, con=conn)
			
			result = pd.merge(result, cspr_df, how='outer', on=['PPE', 'MDD_code', 'year', 'month'])
			# NAN PROBLEMS !!!!!!!!!!!!!!!!!!!
	finally:			
		conn.close()

	return result
	# EXTRACT(day FROM ENERGY100_A.I_DATETIME) "day", 

def save_cspr_data(cspr, user_data):

	
# wyciagnąć dane dla wszystkich dni z zakresu i dodać kolumny w dataframie - done


#potem podział na te które sa i ich nie ma
#bulk insert dla nieistniejacych

#update dla pozostałych  - zrobione tylko pod cspr podstawić te które są
	object_data={}
	one_day_dict={}
	for index, row in cspr.iterrows():
		month=row['month']
		year=row['year']
		PPE=row['PPE']
		SE=row['MDD_code']
		for g in range (1,32):
			try:
				one_day_dict={'value_d'+str(g): row['ener_'+str(g)], 'status_d'+str(g): row['status_'+str(g)], 
				'tariff_d'+str(g):row['tariff_'+str(g)], 'SE':row['MDD_code'], 'user':user_data}
			except KeyError:
				pass
			object_data.update(one_day_dict)

		CSPR_data.save_cspr_obj(PPE, year, month, SE, object_data)


def cspr_handle(user_data):
	fetched=fetch_cspr_data()
	save_cspr_data(fetched, user_data)