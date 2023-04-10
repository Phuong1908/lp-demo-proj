from constants import DATA_DIR
import numpy as np
from problem import Problem

def intersection(list1, list2):
  result = [value for value in list1 if value in list2]
  return result 

def build_problem(name):
  datapath = f'{DATA_DIR}{name}.txt'
  with open(datapath) as file:
    dims = file.readline().strip().split(' ')# read first line
    costs = np.array(file.readline().split(' '),int) # read 2nd line
    row_covered_list = []
    for line in file:
      if not line.strip(): #remove empty line
          continue
      row_covered_list.append(np.array(line.split(' '),int))
  return Problem(name, dims[0], dims[1], costs, row_covered_list)
    
