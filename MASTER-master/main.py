from master import MASTERModel
import pickle
import numpy as np
import time
import pandas as pd
import torch
from preprocessing import *
# Please install qlib first before load the data.

data_dir = f'data'
market = 'Market' # ['Market','SP500']

df_train, df_test, start_index, end_index = data_preprocessing(f"./{data_dir}/CRSP_alpha_new.pqt", f"./{data_dir}/{market}_feature.pqt") 
# OPENPRC

print("Data Loaded.")


d_feat = start_index 
d_model = 128
t_nhead = 4
s_nhead = 2
dropout = 0.5
gate_input_start_index = start_index
gate_input_end_index = end_index 

beta = 5

n_epoch = 100
lr = 1e-6
GPU = 0
train_stop_loss_thred = 0.95


ic = []
icir = []
ric = []
ricir = []

# Training
######################################################################################
for seed in [0, 1, 2, 3, 4]:
    model = MASTERModel(
        d_feat = d_feat, d_model = d_model, t_nhead = t_nhead, s_nhead = s_nhead, T_dropout_rate=dropout, S_dropout_rate=dropout,
        beta=beta, gate_input_end_index=gate_input_end_index, gate_input_start_index=gate_input_start_index,
        n_epochs=n_epoch, lr = lr, GPU = GPU, seed = seed, train_stop_loss_thred = train_stop_loss_thred,
        save_path='model', save_prefix=f'{market}'
    )

    start = time.time()
    # Train
    # model.fit(df_train, df_valid)
    model.fit(df_train)
    print("Model Trained.")

    # Test
    predictions, metrics = model.predict(df_test)
    
    running_time = time.time()-start
    
    print('Seed: {:d} time cost : {:.2f} sec'.format(seed, running_time))
    print(metrics)

    ic.append(metrics['IC'])
    icir.append(metrics['ICIR'])
    ric.append(metrics['RIC'])
    ricir.append(metrics['RICIR'])
######################################################################################

# Load and Test
######################################################################################
# for seed in [0]:
#     param_path = f'model\{universe}_{prefix}_{seed}.pkl'

#     print(f'Model Loaded from {param_path}')
#     model = MASTERModel(
#             d_feat = d_feat, d_model = d_model, t_nhead = t_nhead, s_nhead = s_nhead, T_dropout_rate=dropout, S_dropout_rate=dropout,
#             beta=beta, gate_input_end_index=gate_input_end_index, gate_input_start_index=gate_input_start_index,
#             n_epochs=n_epoch, lr = lr, GPU = GPU, seed = seed, train_stop_loss_thred = train_stop_loss_thred,
#             save_path='model/', save_prefix=universe
#         )
#     model.load_param(param_path)
#     predictions, metrics = model.predict(dl_test)
#     print(metrics)

#     ic.append(metrics['IC'])
#     icir.append(metrics['ICIR'])
#     ric.append(metrics['RIC'])
#     ricir.append(metrics['RICIR'])
    
######################################################################################

print("IC: {:.4f} pm {:.4f}".format(np.mean(ic), np.std(ic)))
print("ICIR: {:.4f} pm {:.4f}".format(np.mean(icir), np.std(icir)))
print("RIC: {:.4f} pm {:.4f}".format(np.mean(ric), np.std(ric)))
print("RICIR: {:.4f} pm {:.4f}".format(np.mean(ricir), np.std(ricir)))