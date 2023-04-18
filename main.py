from tqdm import tqdm
from ga import Individual, Population
from utils import build_problem
from constants import GENERATIONS, POPULATION_SIZE

if __name__ == "__main__":
  problem = build_problem(name='')
	population = Population.create_initial_population(problem=problem)
	best_invi = None
	for i in tqdm(range(GENERATIONS)):
		#evolution phase
		children = population.create_child()
		population.extend(children)
		local_best_indi = population.get_best()
		#evaluate phase
		new_population = Population()
    
