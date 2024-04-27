import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:2401@localhost:5432/PetProject")

files = [
    "campaign_table.csv",
    "causal_data.csv",
    "coupon.csv",
    "coupon_redempt.csv",
]

for file_name in files:
    table_name = file_name.split('.')[0]
    chunksize = 10000
    df = pd.read_csv(f"../../../../Data analysis/SQL pet-project/{file_name}", chunksize=chunksize)

    for chunk in df:
      chunk.to_sql(table_name, engine, index=False, if_exists='append', schema='households_retailer')
