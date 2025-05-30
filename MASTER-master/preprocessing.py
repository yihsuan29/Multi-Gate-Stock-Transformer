import pandas as pd
import numpy as np


data_dir = f'data'
market = 'SP500' # ['Market','SP500']

def data_preprocessing(stock_path, market_path):
    
    df_stock = pd.read_parquet(stock_path)
    df_market = pd.read_parquet(market_path)

    df_stock["date"] = pd.to_datetime(df_stock["date"])
    df_market["date"] = pd.to_datetime(df_market["date"])
    feature_num = df_stock.shape[1] - 7  # 計算feature數量以及市場開始的index
    end_index = feature_num + df_market.shape[1] - 1  #市場結束的index

    
    
    df_merged = pd.merge(df_stock, df_market, on="date", how="left") #合併股票與市場資訊
    df_merged = df_merged.sort_values(by=['PERMNO', 'date']).reset_index(drop=True)

    df_merged = df_merged[df_merged['date'] >= '2008-01-01'] #撇除2008年之前的資料
    df_merged['label'] = df_merged.groupby('PERMNO')['RET'].shift(-1) #新增label(明天的RET)
    df_merged = df_merged.dropna(subset=['label']).reset_index(drop=True)

    bool_cols = df_merged.select_dtypes(include=['bool']).columns #選擇bool類型的欄位
    df_merged[bool_cols] = df_merged[bool_cols].astype(np.int8) #將bool類型轉換為int8

    df_merged['alpha084'].replace([np.inf, -np.inf], np.nan)
    q99 = df_merged['alpha084'].quantile(0.99)
    df_merged['alpha084'] = df_merged['alpha084'].clip(upper=q99)
    df_merged['alpha084'] = np.log(df_merged['alpha084'] + 1e-6)
    df_merged = df_merged.ffill() #將NaN值填充為前一個有效值

    columns_to_remove = ["TICKER", "COMNAM", "SICCD", "NCUSIP", "CUSIP"]
    df_merged = df_merged.drop(columns_to_remove, axis=1)
    df_merged.to_csv('data/View.csv', index=False)

    df_train = df_merged[df_merged['date'] < '2023-01-01']
    df_test = df_merged[df_merged['date'] >= '2023-01-01']
    return df_train, df_test, feature_num, end_index


# print(df_merged['alpha084'].describe())
# print(df_merged['alpha084'].isna().any().any(), np.isinf(df_merged['alpha084'].to_numpy()).any())
# print(df_merged.isna().any().any(), np.isinf(df_merged.to_numpy()).any())
# df_merged.to_csv('data/View.csv', index=False)