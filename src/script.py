# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smessal <smessal@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/29 22:07:04 by smessal           #+#    #+#              #
#    Updated: 2023/06/29 23:30:15 by smessal          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from tabulate import tabulate

result_path = "../results/comparison.xlsx"

df_res = pd.read_excel(result_path)

user_input = "yes"

while 1:
	user_input = input("Entrez le nom du medicament recherché: ")
	if user_input == "stop":
		break
	filtered_df = df_res[df_res["Medicament"].str.startswith(user_input.upper())]
	filtered_df = filtered_df.assign(Length=filtered_df["Medicament"].str.len())
	filtered_df = filtered_df.sort_values(by=["Length"])
	filtered_df = filtered_df.drop("Length", axis=1)
	# filtered_df = filtered_df.style.background_gradient(cmap='Blues').highlight_max(axis=0)
	# display(filtered_df.style)
	print(tabulate(filtered_df[:10], headers='keys', tablefmt='psql'))
	print("\n\n")
	