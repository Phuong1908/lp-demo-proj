import numpy as np
import random
import copy
from utils import intersection
from constants import ALPHA, POPULATION_SIZE, TOURNAMENT_PARTICIPANTS, TOURNAMENT_SELECTION_PROB, MUTATION_PROB, NUM_OF_MUTATED_GENES

class Individual:
  def __init__(self, length):
    self.length = length
    self.features = np.array([random.randint(0, 1) for _ in range(0,length)])
    self.rank = None
    self.fitness = None
    self.cost = None
    self.uncovered_count = None
  
  def __str__(self):
    return ','.join(map(str, self.features))
  
  def calc_cost(self, cost_list):
    self.cost = np.dot(self.features, cost_list)
  
  def get_uncovered_count(self, row_covered_list):
    count = 0
    self_cover_row_indexes = np.where(self.features == 1) #return tuple
    self_cover_rows = list(map(lambda x: x + 1, self_cover_row_indexes[0]))
    for row_covered_data in row_covered_list:
      if not intersection(self_cover_rows, row_covered_data):
        count += 1
    self.uncovered_count = count
  
  def calc_error(self, cost_list, row_covered_list):
    max_cost = np.max(np.multiply(self.features, cost_list))
    self.get_uncovered_count(row_covered_list)
    return ALPHA*self.uncovered_count*max_cost
    
  def calc_fitness(self, cost_list, row_covered_list): #aim to maximize fitness <-> minimize cost
    max_cost_value = np.sum(cost_list)
    self.calc_cost(cost_list)
    fitness_value = max_cost_value - (self.calc_error(cost_list=cost_list, row_covered_list=row_covered_list) + self.cost)
    if fitness_value < 0:
      fitness_value = 0
    self.fitness = fitness_value
  
  # def calc_fitness(self, cost_list, row_covered_list): #aim to maximize fitness <-> minimize cost
  #   self.fitness =  1 / (self.calc_error(cost_list=cost_list, row_covered_list=row_covered_list) + self.calc_cost(cost_list=cost_list) + 1)
    
  def simple_invert_mutate(self):
    #simple invert mutation
    start_index = random.randint(0, self.length - 1)
    end_index = random.randint(0, self.length - 1)
    if start_index > end_index:
      start_index, end_index = end_index, start_index
    while start_index < end_index:
      self.features[start_index], self.features[end_index] = self.features[end_index], self.features[start_index]
      start_index +=1
      end_index -= 1
      
  def simple_invert_mutate_with_prob(self):
    if random.random() < MUTATION_PROB:
        self.simple_invert_mutate()
      
  def random_flip_mutate(self):
    for i in range(self.length):
      if random.random() < MUTATION_PROB:
        self.features[i] = 1 - self.features[i]
  
  def random_flip_mutate_in_range(self):
    if random.random() < MUTATION_PROB:
      start_point = random.randint(0, self.length - 1)
      mutated_range = NUM_OF_MUTATED_GENES
      if start_point + NUM_OF_MUTATED_GENES > self.length:
        mutated_range = self.length - start_point
      for i in range(0, mutated_range):
        self.features[start_point + i] = 1 - self.features[start_point + i]
  
  @staticmethod
  def crossover(individual_1, individual_2):
    length = len(individual_1.features)
    cut_point = random.randint(0, length - 1)
    first_child = Individual(length=length)
    second_child = Individual(length=length)
    first_child.features = np.append(individual_1.features[0:cut_point], individual_2.features[cut_point:length])
    second_child.features = np.append(individual_2.features[0:cut_point], individual_1.features[cut_point:length])
    return first_child, second_child
  
  @staticmethod
  def two_points_crossover(individual_1, individual_2):
    length = len(individual_1.features)
    first_cut_point = random.randint(0, length - 1)
    second_cut_point = first_cut_point
    
    while second_cut_point == first_cut_point:
      second_cut_point = random.randint(0, length - 1)
    if first_cut_point > second_cut_point:
      first_cut_point, second_cut_point = second_cut_point, first_cut_point

    first_child = copy.deepcopy(individual_1)
    second_child = copy.deepcopy(individual_2)
    
    for i in range(first_cut_point, second_cut_point):
      first_child.features[i], second_child.features[i] = second_child.features[i], first_child.features[i]
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
  
  def tournament_selection(self):
    participants = random.sample(self.population, TOURNAMENT_PARTICIPANTS)
    sorted_participants = sorted(participants, key=lambda x: x.fitness, reverse=True)
    for participant in sorted_participants:
      if random.random() <= TOURNAMENT_SELECTION_PROB:
          return participant
    return sorted_participants[0]
  
  # def __cal_prob(self):
  #   rank_sum = POPULATION_SIZE * (POPULATION_SIZE + 1) / 2
  #   population_fitness = map(lambda indi: indi.fitness , self.population)
  #   for rank, ind_fitness in enumerate(sorted(population_fitness), 1):
  #     yield rank, ind_fitness, float(rank) / rank_sum
      
  def create_child(self):
    children = []
    while len(children) < POPULATION_SIZE:
      parent1 = self.tournament_selection()
      parent2 = None
      while parent2 == parent1 or parent2 is None:
          parent2 = self.tournament_selection()
      child1, child2 = Individual.crossover(parent1, parent2)
      child1.random_flip_mutate_in_range()
      child2.random_flip_mutate_in_range()
      child1.calc_fitness(cost_list=self.cost_list, row_covered_list=self.row_covered_list)
      child2.calc_fitness(cost_list=self.cost_list, row_covered_list=self.row_covered_list)
      children.append(child1)
      children.append(child2)
    return children
      
  def get_best(self):
    # return the best feasible solution
    sorted_pop = sorted(self.population, key=lambda x: x.fitness, reverse=True)
    for individual in sorted_pop:
      if individual.get_uncovered_count(row_covered_list=self.row_covered_list) == 0:
        return individual
      
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
  
  def print(self):
    for individual in self.population:
      print(individual.cost)
    print("======")
