import gymnasium as gym
import pytest
from stable_baselines3.common.env_checker import check_env

import pybullet_envs_gymnasium  # noqa: F401

BULLET_ENVS = [env_id for env_id, value in gym.envs.registry.items() if "bullet_envs_gymnasium" in str(value.entry_point)]


@pytest.mark.parametrize("env_id", BULLET_ENVS)
def test_envs(env_id):
    env = gym.make(env_id)
    check_env(env)
