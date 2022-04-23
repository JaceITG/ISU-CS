#!/usr/bin/env python3
import urllib.request

valid_state = lambda x : x.isalpha() and len(x)==2

def read_csv(file_path, field_sep=",", record_sep="\n"):
    cnt = ""

    with urllib.request.urlopen(file_path) as req:
        cnt = req.read().decode("utf-8")
        
    lines = cnt.split(record_sep)

    header = lines.pop(0).split(field_sep)[1:]

    #dict of dicts {ID: {string:string}}
    data = {}
    for l in lines:
        #skip empty lines
        if len(l) < 1:
            continue

        values = l.split(field_sep)

        first = values.pop(0)
        id = int(first) if first.isdigit() else first
        
        data[id] = {header[i]:values[i] for i in range(len(values))}
    
    return data

def format_dollar(num):
    num = round(num,2)
    return f"$ {num:,.02f}"

tax_rates = read_csv("https://cs.indstate.edu/~lmay1/assets/sales-data/tax.csv")
def customer_tax_rate(customer):

    state = customer['State']
    if not state:
        tax_rate = 0
    else:
        #validate state
        if not valid_state(state):
            #State got swapped, find
            for k in customer.keys():
                if valid_state(customer[k]):
                    state = customer[k]
                    break

        tax_rate = float(tax_rates[state_abv_to_name(state)]['Rate'][:-1])
        tax_rate /= 100
    return tax_rate

def state_abv_to_name(abv):
    states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
    }
    return states[abv]