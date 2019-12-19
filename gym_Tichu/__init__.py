from gym.envs.registration import register

register(
    id='Tichu-v0',
    entry_point='gym_Tichu.envs:TichuEnv',
)