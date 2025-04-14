import gymnasium as gym
from . import agents

'''
    Register the LegRobot-planar-walk-v0 and LegRobot-planar-walk-play-v0 environments
'''
gym.register(
    id="LegRobot-planar-walk-v1",
    entry_point=f"{__name__}.leg_planar_walk:LegPlanarWalkEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.leg_leap_cfg:LegPlanarWalkEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:LegPlanarWalkPPORunnerCfg",
    },
)

gym.register(
    id="LegRobot-planar-walk-play-v1",
    entry_point=f"{__name__}.leg_planar_walk:LegPlanarWalkEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.leg_leap_cfg:LegPlanarWalkPlayEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:LegPlanarWalkPPORunnerCfg",
    },
)

'''
    Register the 
'''
gym.register(
    id="LegRobot-leap-v1",
    entry_point=f"{__name__}.leg_leap:LegLeapEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.leg_leap_cfg:LegLeapEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:LegLeapPPORunnerCfg",
    },
)

gym.register(
    id="LegRobot-leap-play-v1",
    entry_point=f"{__name__}.leg_leap:LegLeapEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.leg_leap_cfg:LegLeapPlayEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:LegLeapPPOPlayRunnerCfg",
    },
)
