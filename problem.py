class Problem:
  def __init__(self, name, m, n, costs, row_covered_list, optimal_sol = None):
    self.name = name
    self.m = m
    self.n = n
    self.costs = costs
    self.row_covered_list = row_covered_list
    self.optimal_sol = optimal_sol
  
  def set_optimal_sol(self, value):
    self.optimal_sol = value
