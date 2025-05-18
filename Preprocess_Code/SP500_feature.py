import pandas as pd

def add_features(df):
    df['Return'] = df['close'].pct_change()

    windows = [5, 10, 20, 30, 60]

    for w in windows:
        df[f'MeanReturn_{w}'] = df['Return'].rolling(w).mean()
        df[f'StdReturn_{w}'] = df['Return'].rolling(w).std()

        rolling_mean_volume = df['volume'].rolling(w).mean()
        df[f'TurnoverRatio_{w}'] = rolling_mean_volume / df['volume']

    for w in windows:
        df[f'MeanTurnover_{w}'] = df[f'TurnoverRatio_{w}'].rolling(w).mean()
        df[f'StdTurnover_{w}'] = df[f'TurnoverRatio_{w}'].rolling(w).std()
        
    if 'TurnoverRatio_5' in df.columns:
        turnover_cols = [f'TurnoverRatio_{w}' for w in windows]
        df.drop(columns=turnover_cols, inplace=True, errors='ignore')

    return df

if __name__ == "__main__":
    df_spy = pd.read_parquet('../Data/SP500/SP500.pqt')
    df_spy = df_spy.rename(columns={'Close': 'close', 'Volume': 'volume'})

    df_spy = df_spy.sort_index()

    df_spy = add_features(df_spy)
    df_spy = df_spy.rename(columns={'Date': 'date'})
    print(df_spy.head(5))
    print(df_spy.tail(5))
    
    for x in df_spy.columns:
        print(x)
        
    df_spy.to_parquet('../Data/SP500/SP500_feature.pqt')
