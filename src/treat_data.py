# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    treat_data.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smessal <smessal@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/27 22:07:17 by smessal           #+#    #+#              #
#    Updated: 2023/06/27 23:40:49 by smessal          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

# URL or file path of the Excel file
zen_path = "../price_lab_priv/zen_price.xlsx"
teva_path = "../price_lab_priv/teva_price.xlsx"
# Read the Excel file into a DataFrame
df_zen = pd.read_excel(zen_path)
df_teva = pd.read_excel(teva_path)
# Display the DataFrame
# print(df_zen.info())

raw_libele = []
for i in df_zen["Libellé article"]:
	raw_libele.append(i.replace("ZEN", "torep"))

# print(df_zen.iloc[300])

print("Result ZEN VS TEVA\n")

j = 0
for i in raw_libele:
	keep = df_teva.loc[df_teva["Libellé article"] == i.replace("torep", "TEV"), 'TAUX %'].any()
	if (keep and int(df_zen["TAUX %"][j].replace(",", "").replace("%", "")) < int(df_teva.loc[df_teva["Libellé article"] == i.replace("torep", "TEV"), 'TAUX %'].values[0].replace(",", "").replace("%", ""))):
		found = df_teva.loc[df_teva["Libellé article"] == i.replace("torep", "TEV")]
		print(df_zen.loc[j, 'Libellé article'], df_zen.loc[j, 'TAUX %'])
		print(found.values[0][2], found.values[0][3])
		print("\n")
	j = j + 1
