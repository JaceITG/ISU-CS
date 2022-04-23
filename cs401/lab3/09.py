#!/usr/bin/env python3
from utils import customer_tax_rate, format_dollar, read_csv, format_dollar

url = "https://cs.indstate.edu/~lmay1/assets/sales-data/sales-{0:02}.csv"

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

monthly_sales = {month_names[i]: read_csv(url.format(i+1)) for i in range(12)}

customers = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/customers.csv")

products = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/products.csv")

#Month, $
min_month = (None, -1)
for i in monthly_sales.items():
    month = i[0]
    d = i[1]

    total_rev = 0
    for l in d.items():
        sale = l[1]
        prod_price = float(products[sale['ProductId']]['Price'])
        quan = int(sale['Quantity'])
        customer = customers[int(sale['CustomerId'])]

        tax_rate = customer_tax_rate(customer)
        
        total_rev += prod_price * quan * (1+tax_rate)
    
    if not min_month[0] or total_rev < min_month[1]:
        min_month = (month, total_rev)

print(f"{min_month[0]}, {format_dollar(min_month[1])}")
        

