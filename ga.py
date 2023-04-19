import numpy as np
import random
from utils import intersection
from constants import ALPHA, POPULATION_SIZE

class Individual:
  def __init__(self, length):
    self.length = length
    self.features = np.array([random.randint(0, 1) for _ in range(0,length)])
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
  
  def calc_error(self, cost_list, row_covered_list):
    max_cost = np.max(np.matmul(self.features, cost_list))
    uncovered_count = self.get_uncovered_count(row_covered_list=row_covered_list)
    return ALPHA*uncovered_count*max_cost
    
  def calc_fitness(self, cost_list, row_covered_list): #aim to maximize fitness <-> minimize cost
    self.fitness =  1 / (self.calc_error(cost_list=cost_list, row_covered_list=row_covered_list) + self.calc_cost(cost_list=cost_list) + 1)
  
  def mutate(self):
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
    first_child = Individual(length=length)
    second_child = Individual(length=length)
    first_child.features = np.append(individual_1.features[0:cut_point], individual_2.features[cut_point:length])
    second_child.features = np.append(individual_2.features[0:cut_point], individual_1.features[cut_point:length])
    return first_child, second_child
    
class Population:
  def __init__(self):
    self.population = []
    self.cost_list = None
    self.row_covered_list = None

  def __len__(self):
    return len(self.population)

  def __iter__(self):
    return self.population.__iter__()

  def extend(self, new_individuals):
    self.population.extend(new_individuals)

  def append(self, new_individual):
    self.population.append(new_individual)
    
  def roulette_wheel_selection(self):
    max = sum([c.fitness for c in self.population])
    selection_probs = [c.fitness/max for c in self.population]
    return self.population[np.random.choice(len(self.population), p=selection_probs)]
  
  # def __cal_prob(self):
  #   rank_sum = POPULATION_SIZE * (POPULATION_SIZE + 1) / 2
  #   population_fitness = map(lambda indi: indi.fitness , self.population)
  #   for rank, ind_fitness in enumerate(sorted(population_fitness), 1):
  #     yield rank, ind_fitness, float(rank) / rank_sum
      
  def create_child(self):
    children = []
    while len(children) < POPULATION_SIZE:
      parent1 = self.roulette_wheel_selection()
      parent2 = parent1
      while parent1 == parent2:
          parent2 = self.roulette_wheel_selection()
      child1, child2 = Individual.crossover(parent1, parent2)
      child1.mutate()
      child2.mutate()
      child1.calc_fitness(cost_list=self.cost_list, row_covered_list=self.row_covered_list)
      child2.calc_fitness(cost_list=self.cost_list, row_covered_list=self.row_covered_list)
      children.append(child1)
      children.append(child2)
    return children
      
  def get_best(self):
    sorted_pop = sorted(self.population, key=lambda x: x.fitness, reverse=True)
    return sorted_pop[0]
    
  @staticmethod
  def create_initial_population(problem):
    population = Population()
    population.cost_list = problem.costs
    population.row_covered_list = problem.row_covered_list
    for _ in range(POPULATION_SIZE):
      individual = Individual(length=problem.n)
      individual.calc_fitness(cost_list=population.cost_list, row_covered_list=population.row_covered_list)
      population.append(individual)
    return population
