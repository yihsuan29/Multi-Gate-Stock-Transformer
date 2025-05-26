from master import MASTERModel
import pickle
import numpy as np
import time
from pprint import pprint
import pandas as pd
universe = 'csi300' # ['csi300','csi800']
prefix = 'opensource' # ['original','opensource'], which training data are you using
train_data_dir = f'data'
with open(f'{train_data_dir}\{prefix}\{universe}_dl_train.pkl', 'rb') as f:
    dl_train = pickle.load(f)

date = '2008-01-02'
stock_code = 'SH600000'
idx = dl_train.idx_df.loc[(date, stock_code)] # 日期跟股票可以指到一筆資料 (222,1)
data = dl_train.data_arr[idx]
# print(data)
print(f"data 維度: {data.shape}")

print(dl_train[0].shape)
# 資料是三維的 每取一筆都是一個二維的資料 8*222


# print(dl_train.shape)
# 查看数据形状
print("数据数组形状:", dl_train.data_arr.shape)
print("数据索引形状:", dl_train.data_index.shape)
print("索引数组形状:", dl_train.idx_arr.shape)
print("索引 DataFrame 形状:", dl_train.idx_df.shape)
print("索引映射形状:", dl_train.idx_map.shape)
# print("索引映射数组形状:", dl_train.idx_map2arr.shape)

# 查看每日数据数量
# print("每日数据数量:", dl_train.daily_count)

# 查看数据范围
print("开始索引:", dl_train.start)
print("结束索引:", dl_train.end)
print("开始索引:", dl_train.start_idx)
print("结束索引:", dl_train.end_idx)
print("步长:", dl_train.step_len)

# 查看配置信息
#print("配置信息:", dl_train.__dict__)
# print(dl_train.idx_df)
# print([method for method in dir(dl_train) if not method.startswith('_')])
# with open(f'{train_data_dir}\{prefix}\{universe}_dl_train.pkl', 'rb') as f:
#     dl_train = pickle.load(f)
    # dl_train.data
    
# print(dl_train)

# df = pd.read_parquet('data/Market_feature.pqt')
# df_sp500 = pd.read_parquet('data/SP500_feature.pqt')
# df_CRSP = pd.read_parquet('data/CRSP_alpha.pqt')

# df_CRSP.to_csv('data/CRSP_feature.csv')
# # print(df.compare(df))
# print(df_CRSP.head())