from tqdm import tqdm
import argparse
import copy
import numpy as np
from ga import Population
from utils import build_problem
from constants import GENERATIONS, POPULATION_SIZE

if __name__ == "__main__":
  # parse problem name
  parser = argparse.ArgumentParser()
  parser.add_argument("problem_name", help="Name of scp problem")
  args = parser.parse_args()
  problem_name = args.problem_name
  problem = build_problem(name=problem_name)
  print(f'Max cost: {np.sum(problem.costs)}')
  population = Population.create_initial_population(problem=problem)
  best_invi = None
  # for i in tqdm(range(GENERATIONS)):
  for i in range(GENERATIONS):
		# evolution phase
    children = population.create_child()
    population.extend(children)
		# evaluation phase
    new_population = (sorted(population.population, key=lambda x: x.fitness, reverse=True)[0:POPULATION_SIZE])
    best_invi = new_population[0]
    population.population = new_population
    print(f'Best individual of gen {i} has cost: {best_invi.cost}')
  best_feasible = population.get_best()
  print(f'Best feasible solution has cost: {best_feasible.cost}')  
  print(f'Optimal cost is {problem.optimal_sol}')
    
