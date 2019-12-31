from import_export import resources
from .models import tariff_data

class TariffResource(resources.ModelResource):
    class Meta:
        model = tariff_data
        fields=['tariff_date','hour_1','hour_2','hour_3','hour_4','hour_5','hour_6','hour_7','hour_8','hour_9','hour_10','hour_11','hour_12',
        		'hour_13','hour_14','hour_15','hour_16','hour_17','hour_18','hour_19','hour_20','hour_21','hour_22','hour_23','hour_24']