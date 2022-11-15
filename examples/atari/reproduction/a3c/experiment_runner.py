import os

# Cart args ~11k eps to solved no mal - 1500/25 finds act
cart_args = ' --env CartPole-v1 --eval-interval 180 --steps 50000 --lr 1e-3 --beta 2e-5 --t-max 5 --activation 1 --hidden_size 64 --ucb_disable 1000 --ucb_param 10'
# Lunar args ~20k eps to positive no mal
lunar_args = ' --env LunarLander-v2 --eval-interval 550  --steps 100000 --lr 0.0009 --beta 0.00002 --t-max 10 --activation 1 --hidden_size 128 --ucb_disable 1000 --ucb_param 20'
cheetah_args = ' --env LunarLander-v1 --eval-interval 360  --steps 100000 --lr 0.0002 --beta 0.00002 --t-max 5 --activation 1 --hidden_size 128 --ucb_disable 1000 --ucb_param 10'
breakout_args = ' --env BreakoutNoFrameskip-v4 --eval-interval 100  --steps 100000 --lr 7e-4 --ucb_disable 1000 --ucb_param 5'

env_args = breakout_args

mal_args = ' --processes 10 --malicious 3 --mal_type noise'
for seed in range(0, 5):
    print('Seed Begin', seed, mal_args, env_args)
    os.system('python train_a3c.py --seed ' + str(seed) + mal_args + env_args)

mal_args = ' --processes 10 --malicious 3 --mal_type act'
for seed in range(0, 5):
    print('Seed Begin', seed, mal_args, env_args)
    os.system('python train_a3c.py --seed ' + str(seed) + mal_args + env_args)

mal_args = ' --processes 10 --malicious 3 --mal_type sign'
for seed in range(0, 5):
    print('Seed Begin', seed, mal_args, env_args)
    os.system('python train_a3c.py --seed ' + str(seed) + mal_args + env_args)
