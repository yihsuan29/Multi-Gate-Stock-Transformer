import yfinance as yf
import pandas as pd

spy = yf.download('SPY', start='2007-01-01', auto_adjust=False)

if isinstance(spy.columns, pd.MultiIndex):
    spy.columns = spy.columns.get_level_values(0)

spy = spy[['Close', 'Volume']]
spy = spy.reset_index()
spy.index.name = None
spy.columns.name = None
print(spy.head(5))

import yfinance as yf
import pandas as pd

spy = yf.download('SPY', start='2007-01-01', auto_adjust=False)

if isinstance(spy.columns, pd.MultiIndex):
    spy.columns = spy.columns.get_level_values(0)

spy = spy[['Close', 'Volume']]
spy = spy.reset_index()
spy.index.name = None
spy.columns.name = None

print(spy.head(5))

spy.to_parquet('../Data/SP500/SP500.pqt')
