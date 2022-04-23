#!/usr/bin/env python3
from utils import customer_tax_rate, format_dollar, read_csv, format_dollar


url = "https://cs.indstate.edu/~lmay1/assets/sales-data/sales-{0:02}.csv"

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

monthly_sales = {month_names[i]: read_csv(url.format(i+1)) for i in range(12)}

products = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/products.csv")


#Product: revenue
product_quants = {}
for i in monthly_sales.items():
    month = i[0]
    d = i[1]

    total_rev = 0
    for l in d.items():
        sale = l[1]
        quan = int(sale['Quantity'])
        
        product_quants.setdefault(sale['ProductId'], 0)
        product_quants[sale['ProductId']] += quan
    

least = min(product_quants)
print(f"{least}, {product_quants[least]}")
        

