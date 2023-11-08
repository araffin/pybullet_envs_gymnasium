import os
import time
from typing import ClassVar

import gymnasium
import gymnasium.spaces
import gymnasium.utils
import gymnasium.utils.seeding
import numpy as np
import pybullet
from pybullet_utils import bullet_client

try:
    if os.getenv("PYBULLET_EGL"):
        import pkgutil
except ImportError:
    pass


class MJCFBaseBulletEnv(gymnasium.Env):
    """
    Base class for Bullet physics simulation loading MJCF (MuJoCo .xml) environments in a Scene.
    These environments create single-player scenes and behave like normal Gym environments, if
    you don't use multiplayer.
    """

    metadata: ClassVar = {"render_modes": ["human", "rgb_array"], "render_fps": 60}  # type: ignore[misc]

    def __init__(self, robot, render_mode=None):
        self.scene = None
        self.physicsClientId = -1
        self.ownsPhysicsClient = 0
        self.camera = Camera(self)
        self.render_mode = render_mode
        self.should_render = render_mode == "human"
        self.robot = robot
        self.seed()
        self._cam_dist = 3
        self._cam_yaw = 0
        self._cam_pitch = -30
        self._render_width = 320
        self._render_height = 240

        self.action_space = robot.action_space
        self.observation_space = robot.observation_space
        # self.reset()

    def configure(self, args):
        self.robot.args = args

    def seed(self, seed=None):
        self.np_random, seed = gymnasium.utils.seeding.np_random(seed)
        self.robot.np_random = self.np_random  # use the same np_randomizer for robot as for env
        return [seed]

    def reset(self, seed=None, options=None):
        if seed is not None:
            self.seed(seed)

        if self.physicsClientId < 0:
            self.ownsPhysicsClient = True

            if self.should_render:
                self._p = bullet_client.BulletClient(connection_mode=pybullet.GUI)
            else:
                self._p = bullet_client.BulletClient()
            self._p.resetSimulation()
            self._p.setPhysicsEngineParameter(deterministicOverlappingPairs=1)
            # optionally enable EGL for faster headless rendering
            try:
                if os.environ["PYBULLET_EGL"]:
                    con_mode = self._p.getConnectionInfo()["connectionMethod"]
                    if con_mode == self._p.DIRECT:
                        egl = pkgutil.get_loader("eglRenderer")
                        if egl:
                            self._p.loadPlugin(egl.get_filename(), "_eglRendererPlugin")
                        else:
                            self._p.loadPlugin("eglRendererPlugin")
            except Exception:
                pass
            self.physicsClientId = self._p._client
            self._p.configureDebugVisualizer(pybullet.COV_ENABLE_GUI, 0)

        if self.scene is None:
            self.scene = self.create_single_player_scene(self._p)
        if not self.scene.multiplayer and self.ownsPhysicsClient:
            self.scene.episode_restart(self._p)

        self.robot.scene = self.scene

        self.frame = 0
        self.done = 0
        self.reward = 0
        s = self.robot.reset(self._p)
        self.potential = self.robot.calc_potential()
        return s.astype(np.float32), {}

    def camera_adjust(self):
        pass

    def render(self):
        if self.render_mode == "human":
            self.should_render = True
        if self.physicsClientId >= 0:
            self.camera_adjust()

        if self.render_mode != "rgb_array":
            time.sleep(1 / self.metadata["render_fps"])
            return

        base_pos = [0, 0, 0]
        if hasattr(self, "robot"):
            if hasattr(self.robot, "body_real_xyz"):
                base_pos = self.robot.body_real_xyz
        if self.physicsClientId >= 0:
            view_matrix = self._p.computeViewMatrixFromYawPitchRoll(
                cameraTargetPosition=base_pos,
                distance=self._cam_dist,
                yaw=self._cam_yaw,
                pitch=self._cam_pitch,
                roll=0,
                upAxisIndex=2,
            )
            proj_matrix = self._p.computeProjectionMatrixFOV(
                fov=60, aspect=float(self._render_width) / self._render_height, nearVal=0.1, farVal=100.0
            )
            (_, _, px, _, _) = self._p.getCameraImage(
                width=self._render_width,
                height=self._render_height,
                viewMatrix=view_matrix,
                projectionMatrix=proj_matrix,
                renderer=pybullet.ER_BULLET_HARDWARE_OPENGL,
            )

            self._p.configureDebugVisualizer(self._p.COV_ENABLE_SINGLE_STEP_RENDERING, 1)
        else:
            px = np.array([[[255, 255, 255, 255]] * self._render_width] * self._render_height, dtype=np.uint8)
        rgb_array = np.array(px, dtype=np.uint8)
        rgb_array = np.reshape(np.array(px), (self._render_height, self._render_width, -1))
        rgb_array = rgb_array[:, :, :3]
        return rgb_array

    def close(self):
        if self.ownsPhysicsClient:
            if self.physicsClientId >= 0:
                self._p.disconnect()
        self.physicsClientId = -1

    def HUD(self, state, a, done):
        pass


class Camera:
    def __init__(self, env):
        self.env = env
        pass

    def move_and_look_at(self, i, j, k, x, y, z):
        lookat = [x, y, z]
        camInfo = self.env._p.getDebugVisualizerCamera()

        distance = camInfo[10]
        pitch = camInfo[9]
        yaw = camInfo[8]
        self.env._p.resetDebugVisualizerCamera(distance, yaw, pitch, lookat)
