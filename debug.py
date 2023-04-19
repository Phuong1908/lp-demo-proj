from ga import Individual, Population
import numpy as np
if __name__ == "__main__":
  indi1 = Individual(length=6)
  indi2 = Individual(length=6)
  cost_list = np.array([1,2,3,4,5,6])
  cover_list = [[1,2,6], [2,3], [3,4], [4,5]]
  indi1.calc_fitness(cost_list=cost_list, row_covered_list=cover_list)
  print(indi1.fitness)
  indi2.calc_fitness(cost_list=cost_list, row_covered_list=cover_list)
  print(indi2.fitness)
  population = Population()
  population.population = [indi1, indi2]
  population.roulette_wheel_selection()