import pandas as pd
import os

def load_data(file_path):
    CRSP_df = pd.read_parquet(os.path.join(file_path, 'CRSP_alpha.pqt'))
    Market_df = pd.read_parquet(os.path.join(file_path, 'Market_feature.pqt'))
    Ind_df = pd.read_parquet(os.path.join(file_path, 'Ind_feature.pqt'))
    Fama_df = pd.read_csv(os.path.join('../Data/Industry', 'Fama12_mapping.csv'))
    return CRSP_df, Market_df, Ind_df, Fama_df

def merge_data(CRSP_df, Market_df, Ind_df, Fama_df):
    CRSP_df['date'] = pd.to_datetime(CRSP_df['date'])
    Market_df['date'] = pd.to_datetime(Market_df['date'])
    Ind_df['date'] = pd.to_datetime(Ind_df['date'])
    Fama_df.rename(columns={'Fama': 'fama12'}, inplace=True)
    

    merged_data = pd.merge(CRSP_df, Market_df, on=['date'], how='left')
    merged_data = pd.merge(merged_data, Fama_df, on=['PERMNO'], how='left')
    merged_data = pd.merge(merged_data, Ind_df, on=['date', 'fama12'], how='left')

    return merged_data

if __name__ == "__main__":
    folder_path = '../Data/Preprocessed/'
    CRSP_df, Market_df, Ind_df, Fama_df = load_data(folder_path)
    merged = merge_data(CRSP_df, Market_df, Ind_df, Fama_df)
    filtered = merged[(merged['date'] > '2008-01-01') & (merged['date'] < '2023-12-31')]
    for col in filtered.columns:
        null_count = filtered[col].isnull().sum()
        if null_count > 0:
            print(f"Column '{col}' has {null_count} null values.")
    # merged.to_parquet(os.path.join(folder_path, 'Merged_data.pqt'), index=False)
    # merged.to_csv(os.path.join(folder_path, 'Merged_data.csv'), index=False)
