import numpy as np
import random
from utils import intersection
from constants import ALPHA, POPULATION_SIZE, TOURNAMENT_PARTICIPANT
class Individual:
  def __init__(self, length):
    self.length = length
    self.features = np.array([random.randint(0, 1) for _ in length])
    self.rank = None
    self.fitness = None
  
  def calc_cost(self, cost_list):
    return np.dot(self.features, cost_list)
  
  def get_uncovered_count(self, row_covered_list):
    count = 0
    self_cover_rows = np.where(self.features == 1)
    for row_covered_data in row_covered_list:
      if intersection(self_cover_rows, row_covered_data):
        count += 1
    return count
  
  def calc_error(self, cost_list):
    max_cost = np.max(np.matmul(self.features, cost_list))
    uncovered_count = self.get_uncovered_count()
    return ALPHA*uncovered_count*max_cost
    
  def calc_fitness(self): #aim to maximize fitness <-> minimize cost
    return -(self.calc_error() + self.calc_cost())
  
  def mutation(self):
    #simple invert mutation
    start_index = random.randint(0, self.length - 1)
    end_index = random.randint(0, self.length - 1)
    if start_index > end_index:
      start_index, end_index = end_index, start_index
    while start_index < end_index:
      self.features[start_index], self.features[end_index] = self.features[end_index], self.features[start_index]
      start_index +=1
      end_index -= 1
  
  @staticmethod
  def crossover(individual_1, individual_2):
    length = len(individual_1.features)
    cut_point = random.randint(0, length - 1)
    first_child = np.concatenate(individual_1.features[0:cut_point], individual_2.features[cut_point:length])
    second_child = np.concatenate(individual_2.features[0:cut_point], individual_1.features[cut_point:length])
    return first_child, second_child
    
class Population:
  def __init__(self):
    self.population = []

  def __len__(self):
    return len(self.population)

  def __iter__(self):
    return self.population.__iter__()

  def extend(self, new_individuals):
    self.population.extend(new_individuals)

  def append(self, new_individual):
    self.population.append(new_individual)
    
  def ranking_selections(self):
    rd_num = random.random()
    
  
  def __cal_prob(self):
    rank_sum = POPULATION_SIZE * (POPULATION_SIZE + 1) / 2
    population_fitness = map(lambda indi: indi.fitness , self.population)
    for rank, ind_fitness in enumerate(sorted(population_fitness), 1):
      yield rank, ind_fitness, float(rank) / rank_sum
      
  def create_child(self):
    children = []
    while len(children) < POPULATION_SIZE:
      parent1 = self.__tournament(population)
      parent2 = parent1
      while parent1 == parent2:
          parent2 = self.__tournament(population)
      child1, child2 = self.__crossover(parent1, parent2)
      self.__mutate(child1)
      self.__mutate(child2)
      self.problem.calculate_objectives(child1)
      self.problem.calculate_objectives(child2)
      children.append(child1)
      children.append(child2)

