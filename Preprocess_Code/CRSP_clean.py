import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.read_csv('../Data/CRSP/CRSP.csv')
selected_c = ['PERMNO','TICKER','COMNAM','date','SICCD','NCUSIP','CUSIP','OPENPRC','ASKHI','BIDLO','PRC','RET','VOL']
crsp_df = df[selected_c].copy()

# Convert columns to string
string_cols = ['TICKER', 'COMNAM', 'SICCD', 'NCUSIP', 'CUSIP']
crsp_df[string_cols] = crsp_df[string_cols].astype(str)

# Convert 'date' to datetime
crsp_df['date'] = pd.to_datetime(crsp_df['date'], errors='coerce')

# Convert numeric columns to float
float_cols = ['OPENPRC', 'ASKHI', 'BIDLO', 'PRC', 'RET', 'VOL']
for col in float_cols:
    crsp_df[col] = pd.to_numeric(crsp_df[col], errors='coerce')

# Drop rows with any NaNs in specified numeric columns
dropna_cols = ['OPENPRC', 'ASKHI', 'BIDLO', 'PRC', 'RET', 'VOL']
crsp_df = crsp_df.dropna(subset=dropna_cols)
for col in dropna_cols:
    crsp_df = crsp_df[crsp_df[col] != 0]
crsp_df['AMOUNT'] = crsp_df['PRC'] * crsp_df['VOL']
print(crsp_df[float_cols])

table = pa.Table.from_pandas(crsp_df)
output_file = '../Data/CRSP/CRSP_cleaned.pqt'
pq.write_table(table, output_file)

print(f'CSV file converted to Parquet: {output_file}')