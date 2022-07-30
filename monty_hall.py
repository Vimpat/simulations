# Simulation of the Monty Hall problem
# https://en.wikipedia.org/wiki/Monty_Hall_problem

import numpy as np
from numpy.random import default_rng

rng = default_rng()
# create the host room. 1 is car, 0 is goat
arr = np.array([0,0,1])
correct_initial = 0
correct_modified = 0

for i in range (0, 10000):
  np.random.shuffle(arr)
  # The player chooses a door
  player_choice = rng.integers(0,3)
  
  # the host chooses the door to open
  host_choice = np.delete(np.arange(3), player_choice)
  index = rng.choice(host_choice.shape[0], 1, replace = False)


  # check whether the chosen door contains the goat. If not, choose the other one
  if arr[host_choice[index]] == 1:
    opened_door_index = np.delete(host_choice, index)
  else: 
    opened_door_index = host_choice[index]

  # Simulate the 2 scenarios: the player switches or doesn't switch
  if arr[player_choice] == 1:
    correct_initial = correct_initial + 1
  else:
    correct_modified = correct_modified + 1

# Compare the results
print(correct_initial/10000)
print(correct_modified/10000)