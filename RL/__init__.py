import gymnasium as gym

gym.register(
    id="Isaac-Velocity-Flat-Hexapod-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": "isaaclab_tasks.manager_based.locomotion.velocity.config.hexapod.hexapod_flat_env_cfg:HexapodFlatEnvCfg",
        "rsl_rl_cfg_entry_point": "isaaclab_tasks.manager_based.locomotion.velocity.config.hexapod.agents.rsl_rl_ppo_cfg:HexapodPPORunnerCfg",
    },
)

gym.register(
    id="Isaac-Velocity-Flat-Hexapod-Play-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": "isaaclab_tasks.manager_based.locomotion.velocity.config.hexapod.hexapod_flat_env_cfg:HexapodFlatEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": "isaaclab_tasks.manager_based.locomotion.velocity.config.hexapod.agents.rsl_rl_ppo_cfg:HexapodPPORunnerCfg",
    },
)
