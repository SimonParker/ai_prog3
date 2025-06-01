#simon parker
from robot import *
import numpy as np
import random
import statistics
import matplotlib.pyplot as plt


def setup_cans(env):
  for i in range(env.shape[0]):
    for j in range(env.shape[1]):
      env[i][j] = random.randint(0, 1)
      
      
env = np.zeros((10, 10))
q_mat = np.zeros((pow(3, 5), 5)) #3^5 possible states, 5 actions per state
robby = Robot(env)

N = 5000
m = 200
eta = 0.2
gamma = 0.9
epsilon = 0.1

train_rewards = []
test_rewards = []
setup_cans(env)
epochs = []

#training loop
for episode in range(N + 1): #i want the plot to include episode 5000
  setup_cans(env)
  robby.reset(env)
  state = robby.sense(env)
  for move in range(m):
    action = robby.choose_act(q_mat, epsilon)
    reward = robby.act(action, env) #also updates robby's total reward
    new_state = robby.sense(env)
    state_index = ter_to_dec(state)
    new_state_index = ter_to_dec(new_state)
    q_val = q_mat[state_index][action]
    q_mat[state_index][action] += eta * (reward + gamma * (max(list(q_mat[new_state_index]))) - q_val)
    state = new_state
  if episode % 50 == 0:
    epsilon = epsilon - 0.002 if epsilon != 0 else 0 #hits 0 halfway through training, 2500 episodes
    if episode % 100 == 0:
      epochs.append(episode)
      train_rewards.append(robby.total_reward)

plt.plot(epochs, train_rewards)
plt.savefig("training plot.png")
plt.close()


epsilon = 0.1
#testing loop
for episode in range(N):
  setup_cans(env)
  robby.reset(env)
  state = robby.sense(env)
  for move in range(m):
    action = robby.choose_act(q_mat, epsilon)
    reward = robby.act(action, env)
    new_state = robby.sense(env)
  test_rewards.append(robby.total_reward)

av = statistics.mean(test_rewards)
stdev = statistics.stdev(test_rewards)
print(f"Test Average: {av}, Test Stdev: {stdev}")


