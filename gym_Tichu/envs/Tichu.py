import gym
import numpy as np
import warnings
import cv2

from gym import error, spaces, utils
from gym.utils import seeding

class TichuEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.state = None
        pass

    def step(self, action):
        reward = 0
        done = False

        return self.state, reward, done, {}

    def reset(self):
        self.__init__()

        return self.state

    def render(self, mode='human'):
        img = None
        return img