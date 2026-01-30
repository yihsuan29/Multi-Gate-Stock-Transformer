import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.read_csv('../Data/CRSP/CRSP.csv')
selected_c = ['PERMNO','TICKER','COMNAM','date','SICCD','NCUSIP','CUSIP','OPENPRC','ASKHI','BIDLO','PRC','RET','VOL']
crsp_df = df[selected_c].copy()

# Convert dtypes
string_cols = ['TICKER', 'COMNAM', 'SICCD', 'NCUSIP', 'CUSIP']
crsp_df[string_cols] = crsp_df[string_cols].astype(str)

crsp_df['date'] = pd.to_datetime(crsp_df['date'], errors='coerce')

float_cols = ['OPENPRC', 'ASKHI', 'BIDLO', 'PRC', 'RET', 'VOL']
for col in float_cols:
    crsp_df[col] = pd.to_numeric(crsp_df[col], errors='coerce')

# Drop rows with any NaNs in specified numeric columns
dropna_cols = ['OPENPRC', 'ASKHI', 'BIDLO', 'PRC', 'RET', 'VOL']
crsp_df = crsp_df.sort_values(by=['PERMNO', 'date']) 
crsp_df[dropna_cols] = crsp_df.groupby('PERMNO')[dropna_cols].ffill().bfill()
crsp_df = crsp_df.dropna(subset=dropna_cols)
for col in dropna_cols:
    crsp_df = crsp_df[crsp_df[col] != 0]
crsp_df['AMOUNT'] = crsp_df['PRC'] * crsp_df['VOL']
print(crsp_df[float_cols])


# Clean duplicate and ffill
crsp_df = crsp_df.drop_duplicates(subset=['PERMNO', 'date'], keep='last')
all_dates = pd.Series(crsp_df['date'].sort_values().unique(), name='date')
all_permnos = crsp_df['PERMNO'].unique()
full_index = pd.MultiIndex.from_product([all_permnos, all_dates], names=['PERMNO', 'date'])
crsp_df = crsp_df.set_index(['PERMNO', 'date']).reindex(full_index).sort_index()
crsp_df = crsp_df.groupby(level=0).ffill().bfill().reset_index()

table = pa.Table.from_pandas(crsp_df)
output_file = '../Data/CRSP/CRSP_cleaned.pqt'
pq.write_table(table, output_file)

print(f'CSV file converted to Parquet: {output_file}')