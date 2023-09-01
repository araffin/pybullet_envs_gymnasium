from gymnasium.envs.registration import register

# ------------bullet-------------

register(
    id="InvertedPendulumBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_pendulum_envs:InvertedPendulumBulletEnv",
    max_episode_steps=1000,
    reward_threshold=950.0,
)

register(
    id="InvertedDoublePendulumBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_pendulum_envs:InvertedDoublePendulumBulletEnv",
    max_episode_steps=1000,
    reward_threshold=9100.0,
)

register(
    id="InvertedPendulumSwingupBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_pendulum_envs:InvertedPendulumSwingupBulletEnv",
    max_episode_steps=1000,
    reward_threshold=800.0,
)

register(
    id="ReacherBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_manipulator_envs:ReacherBulletEnv",
    max_episode_steps=150,
    reward_threshold=18.0,
)

register(
    id="PusherBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_manipulator_envs:PusherBulletEnv",
    max_episode_steps=150,
    reward_threshold=18.0,
)

register(
    id="ThrowerBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_manipulator_envs:ThrowerBulletEnv",
    max_episode_steps=100,
    reward_threshold=18.0,
)


register(
    id="Walker2DBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_locomotion_envs:Walker2DBulletEnv",
    max_episode_steps=1000,
    reward_threshold=2500.0,
)
register(
    id="HalfCheetahBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_locomotion_envs:HalfCheetahBulletEnv",
    max_episode_steps=1000,
    reward_threshold=3000.0,
)

register(
    id="AntBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_locomotion_envs:AntBulletEnv",
    max_episode_steps=1000,
    reward_threshold=2500.0,
)

register(
    id="HopperBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_locomotion_envs:HopperBulletEnv",
    max_episode_steps=1000,
    reward_threshold=2500.0,
)

register(
    id="HumanoidBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_locomotion_envs:HumanoidBulletEnv",
    max_episode_steps=1000,
)

register(
    id="HumanoidFlagrunBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_locomotion_envs:HumanoidFlagrunBulletEnv",
    max_episode_steps=1000,
    reward_threshold=2000.0,
)

register(
    id="HumanoidFlagrunHarderBulletEnv-v0",
    entry_point="pybullet_envs_gymnasium.gym_locomotion_envs:HumanoidFlagrunHarderBulletEnv",
    max_episode_steps=1000,
)
