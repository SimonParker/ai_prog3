#simon parker
from robot import *
import numpy as np
import random


def setup_cans(env):
  for i in range(env.shape[0]):
    for j in range(env.shape[1]):
      env[i][j] = random.randint(0, 1)
      
      
env = np.zeros((10, 10))
q_mat = np.zeros((pow(3, 5), 5)) #3^5 possible states, 5 actions per state


