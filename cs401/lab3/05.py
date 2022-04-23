#!/usr/bin/env python3
from utils import read_csv

data = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/customers.csv")

num_switched = 0
for i in data.items():
    d = i[1]
    if (d['Zip'].isalpha() and len(d['Zip'])==2) and (d['State'].isdigit() and len(d['State'])==5):
        num_switched += 1

print(f"{round((num_switched/len(data))*100, 2):.02f} %")