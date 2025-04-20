import optuna
import torch

def objective(trial):
    # Suggest hyperparameters
    lr_a = trial.suggest_loguniform('lr_a', 5e-5, 1e-2)
    lr_c = trial.suggest_loguniform('lr_c', 5e-5, 1e-2)
    gamma = trial.suggest_uniform('gamma', 0.90, 0.999)
    noise_scale = trial.suggest_uniform('noise_scale', 0.1, 0.5)
    step_size = trial.suggest_int('step_size', 100, 300)
    lr_a_decay = trial.suggest_uniform('lr_a_decay', 0.5, 0.99)
    lr_c_decay = trial.suggest_uniform('lr_c_decay', 0.5, 0.99)

    # TensorBoard log path
    logdir = f"Tunning2/lr_a{lr_a:.1e}_lr_c{lr_c:.1e}_gamma{gamma:.3f}_noise{noise_scale:.2f}_stepsize{step_size}_lr_a_decay{lr_a_decay:.2f}_lr_c_decay{lr_c_decay:.2f}"
    os.makedirs(logdir, exist_ok=True)
    writer = SummaryWriter(log_dir=logdir)

    # Modify your train function to accept these arguments
    final_ewma = train(
        env_name="HalfCheetah_CDQ",
        writer=writer,
        gamma=gamma,
        lr_a=lr_a,
        lr_c=lr_c,
        noise_scale=noise_scale,
        step_size=step_size,
        lr_a_decay=lr_a_decay,
        lr_c_decay=lr_c_decay
    )

    writer.close()

    # Objective: maximize final EWMA reward
    return final_ewma



if __name__ == '__main__':
    # For reproducibility
    random_seed = 10
    torch.manual_seed(random_seed)
    env = gym.make('HalfCheetah-v2')
    env.seed(random_seed)

    # Create study
    study = optuna.create_study(direction='maximize', sampler=optuna.samplers.TPESampler(seed=random_seed))
    study.optimize(objective, n_trials=50)