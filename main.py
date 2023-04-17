from problem import Problem
from tqdm import tqdm
from ga import Individual, Population
from utils import build_problem
from constants import GENERATIONS, POPULATION_SIZE

if __name__ == "__main__":
  problem = build_problem(name='')
	population = Population.create_initial_population(problem=problem)
	for i in tqdm(range(GENERATIONS)):
		children = population.create_child()
		population.extend(children)
		new_population = Population()
    #wip