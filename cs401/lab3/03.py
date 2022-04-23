#!/usr/bin/env python3
from utils import read_csv

data = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/customers.csv")

num_empty = 0
for i in data.items():
    d = i[1]
    if not d['Zip']:
        num_empty += 1

print(f"{round((num_empty/len(data))*100, 2):.02f} %")