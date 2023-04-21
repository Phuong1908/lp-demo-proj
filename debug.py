from ga import Individual, Population
import numpy as np
if __name__ == "__main__":
  indi1 = Individual(length=6)
  indi2 = Individual(length=6)
  print(indi1)
  print(indi2)
  cost_list = np.array([1,2,3,4,5,6])
  cover_list = [[1,2,6], [2,3], [3,4], [4,5]]
  child1, child2 = Individual.two_points_crossover(indi1, indi2)
  print('-----')
  print(child1)
  print(child2)
  print(indi1)
  print(indi2)
  
