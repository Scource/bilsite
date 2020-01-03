from django.db import models
from django.conf import settings


class tariff_data(models.Model):
	tariff_date=models.DateField()
	tariff_schemas=models.CharField(max_length=5)
	hour_1=models.FloatField()
	hour_2=models.FloatField()
	hour_3=models.FloatField()
	hour_4=models.FloatField()
	hour_5=models.FloatField()
	hour_6=models.FloatField()
	hour_7=models.FloatField()
	hour_8=models.FloatField()
	hour_9=models.FloatField()
	hour_10=models.FloatField()
	hour_11=models.FloatField()
	hour_12=models.FloatField()
	hour_13=models.FloatField()
	hour_14=models.FloatField()
	hour_15=models.FloatField()
	hour_16=models.FloatField()
	hour_17=models.FloatField()
	hour_18=models.FloatField()
	hour_19=models.FloatField()
	hour_20=models.FloatField()
	hour_21=models.FloatField()
	hour_22=models.FloatField()
	hour_23=models.FloatField()
	hour_24=models.FloatField()

	def __str__(self):
		return self.name

	@classmethod
	def save_1h(cls):
		aa={'tariff_date':'2012-01-04'}
		ob=tariff_data.objects.update_or_create( 
			{'hour_1':1,
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
			'hour_16':1,
			'hour_17':1,
			'hour_18':1,
			'hour_19':1,
			'hour_20':1,
			'hour_21':1,
			'hour_22':1,
			'hour_23':1,
			'hour_24':1,},
			defaults={'tariff_schemas':'C11', 'tariff_date':'2012-01-04'})






class UR_objects(models.Model):
	URB=((0, "POB"),
		(1, "SE")
		)
	code=models.CharField(max_length=25)
	name=models.CharField(max_length=70)
	is_pob=models.IntegerField(choices=URB, default=0)
	DT_create=models.DateField(auto_now_add=True)
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET('deleted'))
	DT_modify=models.DateField(auto_now=True)

	def __str__(self):
		return self.name

class UR_conn(models.Model):
	POB=models.ForeignKey(UR_objects, related_name='POB_id', on_delete=models.CASCADE)
	SE=models.ForeignKey(UR_objects, related_name='SE_id', on_delete=models.CASCADE)
	DT_from=models.DateField()
	DT_to=models.DateField()
	DT_create=models.DateField(auto_now_add=True)
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET('deleted'), null=True)
	DT_modify=models.DateField(auto_now=True)
	
	def __str__(self):
		return self.name


class CSPR_data(models.Model):
	PPE_number=models.CharField(max_length=40)
	month_date=models.DateField()
	value_d1=models.FloatField(null=True)
	value_d2=models.FloatField(null=True)
	value_d3=models.FloatField(null=True)
	value_d4=models.FloatField(null=True)
	value_d5=models.FloatField(null=True)
	value_d6=models.FloatField(null=True)
	value_d7=models.FloatField(null=True)
	value_d8=models.FloatField(null=True)
	value_d9=models.FloatField(null=True)
	value_d10=models.FloatField(null=True)
	value_d11=models.FloatField(null=True)
	value_d12=models.FloatField(null=True)
	value_d13=models.FloatField(null=True)
	value_d14=models.FloatField(null=True)
	value_d15=models.FloatField(null=True)
	value_d16=models.FloatField(null=True)
	value_d17=models.FloatField(null=True)
	value_d18=models.FloatField(null=True)
	value_d19=models.FloatField(null=True)
	value_d20=models.FloatField(null=True)
	value_d21=models.FloatField(null=True)
	value_d22=models.FloatField(null=True)
	value_d23=models.FloatField(null=True)
	value_d24=models.FloatField(null=True)
	value_d25=models.FloatField(null=True)
	value_d26=models.FloatField(null=True)
	value_d27=models.FloatField(null=True)
	value_d28=models.FloatField(null=True)
	value_d29=models.FloatField(null=True)
	value_d30=models.FloatField(null=True)
	value_d31=models.FloatField(null=True)
	status_d1=models.FloatField(null=True)
	status_d2=models.FloatField(null=True)
	status_d3=models.FloatField(null=True)
	status_d4=models.FloatField(null=True)
	status_d5=models.FloatField(null=True)
	status_d6=models.FloatField(null=True)
	status_d7=models.FloatField(null=True)
	status_d8=models.FloatField(null=True)
	status_d9=models.FloatField(null=True)
	status_d10=models.FloatField(null=True)
	status_d11=models.FloatField(null=True)
	status_d12=models.FloatField(null=True)
	status_d13=models.FloatField(null=True)
	status_d14=models.FloatField(null=True)
	status_d15=models.FloatField(null=True)
	status_d16=models.FloatField(null=True)
	status_d17=models.FloatField(null=True)
	status_d18=models.FloatField(null=True)
	status_d19=models.FloatField(null=True)
	status_d20=models.FloatField(null=True)
	status_d21=models.FloatField(null=True)
	status_d22=models.FloatField(null=True)
	status_d23=models.FloatField(null=True)
	status_d24=models.FloatField(null=True)
	status_d25=models.FloatField(null=True)
	status_d26=models.FloatField(null=True)
	status_d27=models.FloatField(null=True)
	status_d28=models.FloatField(null=True)
	status_d29=models.FloatField(null=True)
	status_d30=models.FloatField(null=True)
	status_d31=models.FloatField(null=True)
	tariff_d1=models.FloatField(null=True)
	tariff_d2=models.FloatField(null=True)
	tariff_d3=models.FloatField(null=True)
	tariff_d4=models.FloatField(null=True)
	tariff_d5=models.FloatField(null=True)
	tariff_d6=models.FloatField(null=True)
	tariff_d7=models.FloatField(null=True)
	tariff_d8=models.FloatField(null=True)
	tariff_d9=models.FloatField(null=True)
	tariff_d10=models.FloatField(null=True)
	tariff_d11=models.FloatField(null=True)
	tariff_d12=models.FloatField(null=True)
	tariff_d13=models.FloatField(null=True)
	tariff_d14=models.FloatField(null=True)
	tariff_d15=models.FloatField(null=True)
	tariff_d16=models.FloatField(null=True)
	tariff_d17=models.FloatField(null=True)
	tariff_d18=models.FloatField(null=True)
	tariff_d19=models.FloatField(null=True)
	tariff_d20=models.FloatField(null=True)
	tariff_d21=models.FloatField(null=True)
	tariff_d22=models.FloatField(null=True)
	tariff_d23=models.FloatField(null=True)
	tariff_d24=models.FloatField(null=True)
	tariff_d25=models.FloatField(null=True)
	tariff_d26=models.FloatField(null=True)
	tariff_d27=models.FloatField(null=True)
	tariff_d28=models.FloatField(null=True)
	tariff_d29=models.FloatField(null=True)
	tariff_d30=models.FloatField(null=True)
	tariff_d31=models.FloatField(null=True)
	direction=models.IntegerField()
	conn_UR=models.ForeignKey(UR_conn, on_delete=models.PROTECT)
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET('deleted'))
	DT_modify=models.DateField(auto_now=True)

class CSB_data(models.Model):
	PPE_number=models.CharField(max_length=40)
	month_date=models.DateField()
	value_d1=models.FloatField(null=True)
	value_d2=models.FloatField(null=True)
	value_d3=models.FloatField(null=True)
	value_d4=models.FloatField(null=True)
	value_d5=models.FloatField(null=True)
	value_d6=models.FloatField(null=True)
	value_d7=models.FloatField(null=True)
	value_d8=models.FloatField(null=True)
	value_d9=models.FloatField(null=True)
	value_d10=models.FloatField(null=True)
	value_d11=models.FloatField(null=True)
	value_d12=models.FloatField(null=True)
	value_d13=models.FloatField(null=True)
	value_d14=models.FloatField(null=True)
	value_d15=models.FloatField(null=True)
	value_d16=models.FloatField(null=True)
	value_d17=models.FloatField(null=True)
	value_d18=models.FloatField(null=True)
	value_d19=models.FloatField(null=True)
	value_d20=models.FloatField(null=True)
	value_d21=models.FloatField(null=True)
	value_d22=models.FloatField(null=True)
	value_d23=models.FloatField(null=True)
	value_d24=models.FloatField(null=True)
	value_d25=models.FloatField(null=True)
	value_d26=models.FloatField(null=True)
	value_d27=models.FloatField(null=True)
	value_d28=models.FloatField(null=True)
	value_d29=models.FloatField(null=True)
	value_d30=models.FloatField(null=True)
	value_d31=models.FloatField(null=True)
	tariff_d1=models.FloatField(null=True)
	tariff_d2=models.FloatField(null=True)
	tariff_d3=models.FloatField(null=True)
	tariff_d4=models.FloatField(null=True)
	tariff_d5=models.FloatField(null=True)
	tariff_d6=models.FloatField(null=True)
	tariff_d7=models.FloatField(null=True)
	tariff_d8=models.FloatField(null=True)
	tariff_d9=models.FloatField(null=True)
	tariff_d10=models.FloatField(null=True)
	tariff_d11=models.FloatField(null=True)
	tariff_d12=models.FloatField(null=True)
	tariff_d13=models.FloatField(null=True)
	tariff_d14=models.FloatField(null=True)
	tariff_d15=models.FloatField(null=True)
	tariff_d16=models.FloatField(null=True)
	tariff_d17=models.FloatField(null=True)
	tariff_d18=models.FloatField(null=True)
	tariff_d19=models.FloatField(null=True)
	tariff_d20=models.FloatField(null=True)
	tariff_d21=models.FloatField(null=True)
	tariff_d22=models.FloatField(null=True)
	tariff_d23=models.FloatField(null=True)
	tariff_d24=models.FloatField(null=True)
	tariff_d25=models.FloatField(null=True)
	tariff_d26=models.FloatField(null=True)
	tariff_d27=models.FloatField(null=True)
	tariff_d28=models.FloatField(null=True)
	tariff_d29=models.FloatField(null=True)
	tariff_d30=models.FloatField(null=True)
	tariff_d31=models.FloatField(null=True)
	SE_name=models.ForeignKey(UR_objects, on_delete=models.PROTECT)
	user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET('deleted'))
	DT_modify=models.DateField(auto_now=True)



class CSB_raw(models.Model):
	PPE_number=models.CharField(max_length=40)
	sell_DT=models.DateField()
	invoice_DT_from=models.DateField()
	invoice_DT_to=models.DateField()
	volume=models.FloatField()
	zone_1=models.FloatField()
	zone_2=models.FloatField()
	zone_3=models.FloatField()
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET('deleted'))
	DT_modify=models.DateField(auto_now=True)
