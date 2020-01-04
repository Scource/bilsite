from .models import tariff_data

#tutaj classa do wycigania danych z xlsa i obrobienia na dane do modelu

def tardata():
	asd={'hour_1':1,
		'hour_2':1,
		'hour_3':1,
		'hour_4':1,
		'hour_5':1,
		'hour_6':1,
		'hour_7':1,
		'hour_8':1,
		'hour_9':1,
		'hour_10':1,
		'hour_11':1,
		'hour_12':1,
		'hour_13':1,
		'hour_14':1,
		'hour_15':1,
		'hour_16':2,
		'hour_17':1,
		'hour_18':1,
		'hour_19':1,
		'hour_20':1,
		'hour_21':1,
		'hour_22':1,
		'hour_23':1,
		'hour_24':1}
	tariff_date='2012-01-05'
	tariff_schemas='C12B'
	tariff_data.save_1h(asd, tariff_date, tariff_schemas)