import pandas as pd

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    records = []
    for line in lines:
        parts = line.strip().split()
        date = parts[0]
        returns = parts[1:]
        for i, value in enumerate(returns, start=1):
            records.append([date, i, float(value)])

    df = pd.DataFrame(records, columns=['date', 'fama12', 'ind_return'])
    return df

def add_features(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['fama12', 'date'])

    windows = [5, 10, 20, 30, 60]

    for w in windows:
        df[f'Ind_MeanReturn_{w}'] = df.groupby('fama12')['ind_return'].transform(lambda x: x.rolling(w).mean())
        df[f'Ind_StdReturn_{w}'] = df.groupby('fama12')['ind_return'].transform(lambda x: x.rolling(w).std())

    return df


if __name__== "__main__":
    df = read_data('../Data/Industry/12Industry_return_daily.txt')
    df = df.sort_values(by=['date', 'fama12'])
    df = df.reset_index(drop=True)    
    df = add_features(df)
    df.to_parquet('../Data/Preprocessed/Ind_feature.pqt')

