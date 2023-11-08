import gymnasium as gym
import pytest
from gymnasium.utils.env_checker import check_env as gym_check_env
from stable_baselines3.common.env_checker import check_env

import pybullet_envs_gymnasium  # noqa: F401

BULLET_ENVS = [env_id for env_id, value in gym.envs.registry.items() if "bullet_envs_gymnasium" in str(value.entry_point)]


@pytest.mark.parametrize("env_id", BULLET_ENVS)
def test_envs(env_id):
    env = gym.make(env_id)
    # requires a X11 display
    gym_check_env(env, skip_render_check=True)
    check_env(env)
