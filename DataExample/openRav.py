import pandas as pd
df = pd.read_parquet("RavenPack/2000.pqt")
print(df.head(5))

print(df[['RPA_DATE_UTC','ENTITY_NAME','RELEVANCE','CSS']].head(5))

for x in df.columns:
    print(x)