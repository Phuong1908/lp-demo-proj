import numpy as np
import random
from utils import intersection
from constants import ALPHA
class Chromosome:
  def __init__(self, length):
    self.length = length
    self.bit_arr = np.array([random.randint(0, 1) for _ in length])
  
  def calc_cost(self, cost_list):
    return np.dot(self.bit_arr, cost_list)
  
  def get_uncovered_count(self, row_covered_list):
    count = 0
    self_cover_rows = np.where(self.bit_arr == 1)
    for row_covered_data in row_covered_list:
      if intersection(self_cover_rows, row_covered_data):
        count += 1
    return count
  
  def calc_error(self, cost_list):
    max_cost = np.max(np.matmul(self.bit_arr, cost_list))
    uncovered_count = self.get_uncovered_count()
    return ALPHA*uncovered_count*max_cost
    
  def calc_fitness(self):
    return -(self.calc_error() + self.calc_cost())
  
  def mutation(self):
    #simple invert mutation
    start_index = random.randint(0, self.length - 1)
    end_index = random.randint(0, self.length - 1)
    if start_index > end_index:
      start_index, end_index = end_index, start_index
    while start_index < end_index:
      self.bit_arr[start_index], self.bit_arr[end_index] = self.bit_arr[end_index], self.bit_arr[start_index]
      start_index +=1
      end_index -= 1
  
  @classmethod
  def crossover(cls, chromo_1, chromo_2):
    cut_point = random.randint(0, chromo_1.length - 1)
    
    
class Population:
  def __init__(self):
    return

  def selection():
    return
