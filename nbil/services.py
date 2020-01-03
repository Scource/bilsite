from .models import tariff_data

#tutaj classa do wycigania danych z xlsa i obrobienia na dane do modelu

def tardata():
	tariff_data.save_1h()