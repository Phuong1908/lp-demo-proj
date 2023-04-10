import numpy as np
import random
class Chromosome:
  def __init__(self, length):
    self.length = length
    self.bit_arr = np.array([random.randint(0, 1) for _ in length])
  
  def calc_cost(self):
    return
  
  def calc_error(self):
    return
  
  def calc_fitness():
    return
  
  @classmethod
  def crossover(cls):
    return
  
  @classmethod
  def mutation(cls):
    return
    
class Population:
  def __init__(self):
    return

  def selection():
    return
