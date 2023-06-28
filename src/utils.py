import pandas as pd

def	download_data():
	TEV_path = "../price_lab_priv/tev_price.xlsx"
	df_TEV = pd.read_excel(TEV_path)

	# File path of the gen labs
	ARR_path = "../price_lab_priv/ARR_price.xlsx"
	BIO_path = "../price_lab_priv/BIO_price.xlsx"
	CRI_path = "../price_lab_priv/CRI_price.xlsx"
	EG_path = "../price_lab_priv/EG_price.xlsx"
	MYL_path = "../price_lab_priv/MYL_price.xlsx"
	SAN_path = "../price_lab_priv/SAN_price.xlsx"
	ZEN_path = "../price_lab_priv/ZEN_price.xlsx"

	# Read the Excel files into a DataFrame
	df_ARR = pd.read_excel(ARR_path)
	df_BIO = pd.read_excel(BIO_path)
	df_CRI = pd.read_excel(CRI_path)
	df_EG = pd.read_excel(EG_path)
	df_MYL = pd.read_excel(MYL_path)
	df_SAN = pd.read_excel(SAN_path)
	df_ZEN = pd.read_excel(ZEN_path)

	gen_labs = {"TEV":df_TEV, "ARR":df_ARR, "BIO":df_BIO, "CRI":df_CRI, "EG":df_EG, "MYL":df_MYL, "SAN":df_SAN, "ZEN":df_ZEN}
	lab_names = ["TEV", "ARR", "BIO", "CRI", "EG", "MYL", "SAN", "ZEN"]
	count = 0
	for i,j in zip(gen_labs.values(), lab_names):
		gen_labs[j]['TAUX %'] = i['TAUX %'].apply(lambda x: x.replace('%', "").replace(",", ".").replace("-", "")).astype(float)
		count += 1
	return gen_labs

def	get_taux(lab, raw_lib, lib):
	taux = []
	for i in raw_lib:
		keep = lab.loc[lab["Libellé article"] == i.replace("XLAB", lib), 'TAUX %'].any()
		if keep:
			taux.append(lab.loc[lab["Libellé article"] == i.replace("XLAB", lib), 'TAUX %'].values[0])
		else :
			taux.append(0.0)
	return taux