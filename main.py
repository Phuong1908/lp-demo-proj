from tqdm import tqdm
import argparse
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
  population = Population.create_initial_population(problem=problem)
  best_invi = None
  for i in tqdm(range(GENERATIONS)):
		# evolution phase
    children = population.create_child()
    # import pdb;pdb.set_trace()
    population.extend(children)
    new_population = Population()
    local_best_indi = population.get_best()
		# evaluate phase
    new_population.extend(sorted(population.population, key=lambda x: x.fitness, reverse=True)[0:POPULATION_SIZE])
    best_invi = new_population.population[0]
    population = new_population
  print(f'Best solution found has cost {best_invi.calc_cost(cost_list=problem.costs)}')
  print(f'Optimal cost is {problem.optimal_sol}')
    
