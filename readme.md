This is the demo project for ***"Solving set covering problem using genetic algorithm"***

**How to run**
- Run `setup_data.sh` script to download all scp datasets from the OR-library. Data will be downloaded and stored under `/Datasets/raw`.
- Run `process_data.py` script to processed data. Processed data will be stored under `Datasets/processed`.
- Install need packages like tdqm,..
- Run `python3 main.py <problem name>` (ex: `python3 main.py 'scpe1'`) to solve correspoding scp problem.

**Explain project structure**
- `best_solution.txt`: contains all the optimal solutions for correspoding scp datasets. 

**Explain the dataset format**
- number of rows (m), number of columns (n) (1st line)
- the cost of each column c(j), j=1,...,n (2nd line)
- for each row i (i=1,...,m): the number of columns which cover row i followed by a list of the columns which cover row i (from 3rd line to end of file)
