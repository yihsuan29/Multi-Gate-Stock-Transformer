import pandas as pd
df = pd.read_parquet("../Data/News/Mapping/RavMapping.pqt")
print(df[df['TICKER']=='AMZN'])

news = pd.read_parquet("../Data/News/Equity/2020.pqt")
print(news[news['RP_ENTITY_ID']=='0157B1'][['TIMESTAMP_UTC','RP_ENTITY_ID','ENTITY_NAME','CSS']])