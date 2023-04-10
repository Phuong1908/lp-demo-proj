import os
from constants import DATA_DIR

def process(filename):
  with open(f'Datasets/raw/{filename}') as f:
    with open(f'{DATA_DIR}{filename}','w+') as output_f:
      first_line = f.readline()
      output_f.write(first_line.strip() + '\n') # write matrix dimension at the first line
      num_of_col = int(process_line(first_line)[1])
      costs = []
      row = []
      count = 0
      start_reading_content = False
      for line in f:
        if not line.strip():
          continue
        if len(costs) < num_of_col:
          costs.extend(process_line(line))
          start_reading_content = (len(costs) == num_of_col)
          if start_reading_content:
            output_f.write(' '.join(costs) + '\n') # write cost of all column to the 2nd line
            continue
        if start_reading_content:
          if count == 0:
            count = int(process_line(line)[0])
            continue
          if len(row) < count:
            row.extend(process_line(line))
            if len(row) == count:
              output_f.write(' '.join(row) + '\n') # write list of columns cover each row from the 3rd line to end of file
              row = []
              count = 0

def process_line(line):
  return line.strip().split(' ')

if __name__ == "__main__":
  for file in os.listdir('Datasets/raw/'):
    process(file)
