import pandas as pd
import os

files = [
    "hh_demographic.csv",
    "transaction_data.csv",
    "product.csv",
    "campaign_table.csv",
    "campaign_desc.csv",
    "causal_data.csv",
    "coupon.csv",
    "coupon_redempt.csv",
]

dataframes_list = []
for file_name in files:
    dataframe = pd.read_csv(f"../../../../Data analysis/SQL pet-project/{file_name}")
    dataframe.name = file_name
    dataframes_list.append(dataframe)

meta_file_path = "./SqlPetProject/meta.txt"
if not os.path.exists(meta_file_path):
    open(meta_file_path, "w").close()

with open(meta_file_path, "a") as file:
    for dataframe in dataframes_list:
        file.write(f"\n{dataframe.name}\n")

        for column_name, series in dataframe.items():
            max_length = series.astype(str).map(len).max()
            file.write(f"{column_name}: {max_length}, {series.dtype}\n")
