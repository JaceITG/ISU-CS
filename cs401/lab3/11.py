#!/usr/bin/env python3
from utils import format_dollar, read_csv, state_abv_to_name, format_dollar

valid_state = lambda x : x.isalpha() and len(x)==2

url = "https://cs.indstate.edu/~lmay1/assets/sales-data/sales-{0:02}.csv"

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

monthly_sales = {month_names[i]: read_csv(url.format(i+1)) for i in range(12)}

customers = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/customers.csv")

products = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/products.csv")

tax_rates = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/tax.csv")

monthly_expenses = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/expenses.csv")


#Month, $
min_month = (None, -1)
for i in monthly_sales.items():
    month = i[0]
    d = i[1]

    net_prof = 0
    for l in d.items():
        sale = l[1]
        prod_price = float(products[sale['ProductId']]['Price'])
        prod_net = prod_price - float(products[sale['ProductId']]['Cost'])
        quan = int(sale['Quantity'])

        net_prof += (prod_net * quan)
    
    expenses = float(monthly_expenses[month_names.index(month)+1]['Expenses'])

    net_prof -= expenses
    if not min_month[0] or net_prof < min_month[1]:
        min_month = (month, net_prof)

print(f"{min_month[0]}, {format_dollar(min_month[1])}")
        

