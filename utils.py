from constants import DATA_DIR
import numpy as np
from problem import Problem

def intersection(list1, list2):
  result = [value for value in list1 if value in list2]
  return result 

def build_problem(name):
  datapath = f'{DATA_DIR}{name}.txt'
  #load_data
  with open(datapath) as file:
    dims = file.readline().strip().split(' ')# read first line
    costs = np.array(file.readline().split(' '),int) # read 2nd line
    row_covered_list = []
    for line in file:
      if not line.strip(): #remove empty line
          continue
      row_covered_list.append(np.array(line.split(' '),int))
  problem = Problem(name, int(dims[0]), int(dims[1]), costs, row_covered_list)
  problem.set_optimal_sol(load_solution(name))
  return problem
    
def load_solution(name):
  with open('solutions.txt') as file:
    for line in file:
      data = line.strip().split(' ')
      if data[0] == name:
        return data[1]