# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    treat_data.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smessal <smessal@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/27 22:07:17 by smessal           #+#    #+#              #
#    Updated: 2023/06/29 22:39:38 by smessal          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import utils

all_labs = utils.download_data()
longest_df = all_labs['MYL']["Libellé article"]
raw_lib = []
clean_lib = []
for i in longest_df:
	raw_lib.append(i.replace("MYL", "XLAB").replace("MYP", "XLAB").replace("VIA", "XLAB").replace("PFI", "XLAB"))
	clean_lib.append(i.replace("MYL", "").replace("MYP", "").replace("VIA", "").replace("PFI", ""))
	

df_res = pd.DataFrame(columns=["Medicament", "TEV", "ARR", "BIO", "CRI", "EG", "MYL", "SAN", "ZEN"])
df_res["Medicament"] = clean_lib

for i in df_res.columns[1:]:
	df_res[i] = utils.get_taux(all_labs[i], raw_lib, i)
	
max_columns = df_res.iloc[:, 1:].idxmax(axis=1)

# Create a new column with the column name of the maximum value
df_res["Best Lab"] = max_columns

# df_res.to_excel("../results/comparison.xlsx", index=False)