#simon parker
import random
import numpy as np

#this takes a ternary string (state representation for robby) and turns it into an index for the Q-matrix
def ter_to_dec(string):
  result = 0
  for i in range(len(string)):
    result += int(string[i]) * pow(3, len(string) - i - 1)
  return result


class Robot():
  def __init__(self, env):
    self.r = random.randint(0, env.shape[0] - 1)
    self.c = random.randint(0, env.shape[1] - 1)
    self.state = "" #north south east west current, 0: wall, 1: no can, 2: can
    self.total_reward = 0 

  def reset(self, env):
    self.r = random.randint(0, env.shape[0] - 1)
    self.c = random.randint(0, env.shape[1] - 1)
    self.state = ""
    self.total_reward = 0 

  def choose_act(self, q_mat, epsilon):
    row = q_mat[ter_to_dec(self.state)]
    moves = list(np.where(row == max(list(row)))[0]) #a list of best moves in the current state
    m = moves[random.randint(0, len(moves) - 1)]
    if random.random() < epsilon:
      return random.randint(0, 4)
    return m

  def act(self, action, env): #5 possible actions, +10 for picking up can, -5 for hitting wall, -1 for picking up nothing
    reward = 0
    match action:
      case 0: #move north
        if self.r == 0:
          reward -= 5
        else:
          self.r -= 1
      case 1: #move south
        if self.r == env.shape[0] - 1:
          reward -= 5
        else:
          self.r += 1
      case 2: #move east
        if self.c == env.shape[1] - 1:
          reward -= 5
        else:
          self.c += 1
      case 3: #move west
        if self.c == 0:
          reward -= 5
        else:
          self.c -= 1
      case 4: #pickup can
        if env[self.r][self.c] == 1:
          reward += 10
          env[self.r][self.c] = 0
        else:
          reward -= 1
    self.total_reward += reward
    return reward

  def sense(self, env): #env is a numpy array
    state = ""

    if self.r == 0: #north
      state += "0"
    else:
      if env[self.r - 1][self.c] == 0:
        state += "1"
      else:
        state += "2"

    if self.r == env.shape[0] - 1: #south
      state += "0"
    else:
      if env[self.r + 1][self.c] == 0:
        state += "1"
      else:
        state += "2"

    if self.c == env.shape[1] - 1: #east
      state += "0"
    else:
      if env[self.r][self.c + 1] == 0:
        state += "1"
      else:
        state += "2"

    if self.c == 0: #west
      state += "0"
    else:
      if env[self.r][self.c - 1] == 0:
        state += "1"
      else:
        state += "2"

    if env[self.r][self.c] == 0: #current
      state += "1"
    else:
      state += "2"

    self.state = state
    return state

    

