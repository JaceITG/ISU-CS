#!/usr/bin/env python3
from os import read
from utils import customer_tax_rate, format_dollar, read_csv, format_dollar

customers = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/customers.csv")

products = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/products.csv")

month = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/sales-10.csv")
print(len(month.items()))
total = 0
count = 0
for l in month.items():
    sale = l[1]
    prod_price = float(products[sale['ProductId']]['Price'])
    quan = int(sale['Quantity'])
    customer = customers[int(sale['CustomerId'])]

    tax_rate = customer_tax_rate(customer)
    
    total += prod_price * quan * (1+tax_rate)

    count += 1
print(count)

print(format_dollar(total)) 