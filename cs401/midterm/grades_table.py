#!/usr/bin/env python3

import urllib.request, re, json

#parse a csv file into a dictionaries of dictionaries
#scores['Last First'] = {'Assn 1': 100.0, 'Assn 2': 100.0...}
def parse_csv(text):
    lines = text.split('\n')
    header = lines.pop(0)
    header = header.split(',')  #convert header to list of values
    scores = {}

    for entry in lines:
        student_data = entry.split(',')
        student_name = ' '.join(student_data[:2])  #take first two from list as name

        #make dictionary of student's scores for each assignment in header
        student_dict = {}
        for i in range(len(student_data)):
            try:
                student_dict[header[i]] = float(student_data[i])
            except ValueError:
                #store name entries as strings instead
                student_dict[header[i]] = student_data[i]


        scores[student_name] = student_dict

    return scores, header

if __name__ == "__main__":
    with urllib.request.urlopen("https://cs.indstate.edu/~lmay1/assets/fake-grades.csv") as req:
        data = req.read().decode("utf-8")

    scores, header = parse_csv(data)

    #select students based on the criteria, append to list of dicts
    results = []
    with open("me.json", 'r') as f:
        me = json.loads(f.read())   #get first and last name

    #Share same first letters
    regex1 = rf"^{me['last'][0]}.* {me['first'][0]}.*$"

    #Share same second letters
    regex2 = rf"^.{me['last'][1]}.* .{me['first'][1]}.*$"

    #Share same last letters
    regex3 = rf"^.*{me['last'][-1]} .*{me['first'][-1]}$"

    regex = re.compile("|".join([regex1,regex2,regex3]), re.I)

    for s in scores.keys():
        if re.match(regex, s):
            results.append(scores[s])


    #sort results
    results.sort(key = lambda x: (x['Last Name'], x['First Name']))

    total = 0
    for r in results:
        #get average of scores on assignments listed in header
        final = 0
        for asgn in header[2:]:
            final += r[asgn]
        final = final / len(header[2:])
        total += final

        name = f"{r['Last Name']}, {r['First Name']}"[:30]

        print(f"{name:30} | {round(final, 2):3.2f} %")

    print('-'*41)

    average = total / len(results)
    print(f"{'Average':30} | {round(average, 2):3.2f} %")
