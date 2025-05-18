import pandas as pd

# Load Macro Daily
Macro = pd.read_parquet('../Data/Market/Macro_daily.pqt')
Macro['date'] = pd.to_datetime(Macro['date'])
Macro = Macro[Macro['date'] >= '2007-01-01']

# Load news
selected_columns = ['RPA_DATE_UTC','RELEVANCE','EVENT_SENTIMENT_SCORE'\
                   ,'CSS','NIP','PEQ','BEE','BMQ','BAM','BCA','BER','MCQ']
news = []
for year in range(2007, 2024):
    file_path = f'../Data/News/Macro/{year}.pqt'
    new = pd.read_parquet(file_path)
    new = new[selected_columns]
    news.append(new)
News = pd.concat(news, ignore_index=True)
News['EVENT_SENTIMENT_SCORE'] = News['EVENT_SENTIMENT_SCORE'].fillna(0)
News = News.groupby('RPA_DATE_UTC').mean().reset_index()
News = News.rename(columns={'RPA_DATE_UTC': 'date'})
News['date'] = pd.to_datetime(News['date'])

# Load S&P500
SP500 = pd.read_parquet('../Data/Preprocessed/SP500_feature.pqt')
SP500['date'] = pd.to_datetime(SP500['date'])

# Merge (left join) on date
merged = SP500.merge(Macro, on='date', how='left')
merged = merged.merge(News, on='date', how='left')
merged = merged[(merged['date'] >= '2007-01-01') & (merged['date'] <= '2023-12-31')]
print(merged.shape)

merged.to_parquet('../Data/Preprocessed/Market_feature.pqt')
