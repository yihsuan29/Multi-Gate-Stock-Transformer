'''
Code from MASTER "https://github.com/SJTU-DMTai/MASTER/blob/master"
'''

from master import MASTERModel
import pickle
import numpy as np
import time

# Please install qlib first before load the data.

universe = 'csi300' # ['csi300','csi800']
prefix = 'opensource' # ['original','opensource'], which training data are you using
train_data_dir = f'data'
with open(f'{train_data_dir}\{prefix}\{universe}_dl_train.pkl', 'rb') as f:
    dl_train = pickle.load(f)

predict_data_dir = f'data\opensource'
with open(f'{predict_data_dir}\{universe}_dl_valid.pkl', 'rb') as f:
    dl_valid = pickle.load(f)
with open(f'{predict_data_dir}\{universe}_dl_test.pkl', 'rb') as f:
    dl_test = pickle.load(f)

print("Data Loaded.")


d_feat = 158 #[alpha001~alpha101 + ravenpack]
d_model = 256
t_nhead = 4
s_nhead = 2
dropout = 0.5
gate_input_start_index = 158 #[market retuen]
gate_input_end_index = 221 #[macro 最後一個 ravenpack]
ind_index_column = 'fama12'
ind_gate_input_start_index = 222 #[industry return]
ind_gate_input_end_index =-1 #[industry mean return]

"""
train dataset
[identifier |individual features(alpha + rav)|market features(sp500 + macro) | fama12 index | industry features (return)]
"""

if universe == 'csi300':
    beta = 5
elif universe == 'csi800':
    beta = 2

n_epoch = 1
lr = 1e-5
GPU = 0
train_stop_loss_thred = 0.95


ic = []
icir = []
ric = []
ricir = []

# Training
######################################################################################
'''for seed in [0, 1, 2, 3, 4]:
    model = MASTERModel(
        d_feat = d_feat, d_model = d_model, t_nhead = t_nhead, s_nhead = s_nhead, T_dropout_rate=dropout, S_dropout_rate=dropout,
        beta=beta, gate_input_end_index=gate_input_end_index, gate_input_start_index=gate_input_start_index,
        n_epochs=n_epoch, lr = lr, GPU = GPU, seed = seed, train_stop_loss_thred = train_stop_loss_thred,
        save_path='model', save_prefix=f'{universe}_{prefix}'
    )

    start = time.time()
    # Train
    model.fit(dl_train, dl_valid)

    print("Model Trained.")

    # Test
    predictions, metrics = model.predict(dl_test)
    
    running_time = time.time()-start
    
    print('Seed: {:d} time cost : {:.2f} sec'.format(seed, running_time))
    print(metrics)

    ic.append(metrics['IC'])
    icir.append(metrics['ICIR'])
    ric.append(metrics['RIC'])
    ricir.append(metrics['RICIR'])'''
######################################################################################

# Load and Test
######################################################################################
for seed in [0]:
    param_path = f'model\{universe}_{prefix}_{seed}.pkl'

    print(f'Model Loaded from {param_path}')
    model = MASTERModel(
            d_feat = d_feat, d_model = d_model, t_nhead = t_nhead, s_nhead = s_nhead, T_dropout_rate=dropout, S_dropout_rate=dropout,
            beta=beta, gate_input_end_index=gate_input_end_index, gate_input_start_index=gate_input_start_index,
            n_epochs=n_epoch, lr = lr, GPU = GPU, seed = seed, train_stop_loss_thred = train_stop_loss_thred,
            save_path='model/', save_prefix=universe
        )
    model.load_param(param_path)
    predictions, metrics = model.predict(dl_test)
    print(metrics)

    ic.append(metrics['IC'])
    icir.append(metrics['ICIR'])
    ric.append(metrics['RIC'])
    ricir.append(metrics['RICIR'])
    
######################################################################################

print("IC: {:.4f} pm {:.4f}".format(np.mean(ic), np.std(ic)))
print("ICIR: {:.4f} pm {:.4f}".format(np.mean(icir), np.std(icir)))
print("RIC: {:.4f} pm {:.4f}".format(np.mean(ric), np.std(ric)))
print("RICIR: {:.4f} pm {:.4f}".format(np.mean(ricir), np.std(ricir)))