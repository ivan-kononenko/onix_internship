import csv
import json

def mygen():
    for x in range(5, 91):
        yield x


def f1(x):
    return x/(x+100)


def f2(x):
    return 1/x


def f3(x):
    return 20*(f1(x) + f2(x))/x


result_dict = {}
for x in mygen():
    result_dict[x] = [f1(x), f2(x), f3(x)]


with open('result.csv', 'w') as result_csv:
    result_csv_writer = csv.writer(result_csv, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for x in mygen():
        result_csv_writer.writerow([x, f1(x), f2(x), f3(x)])


with open('result.csv', 'r') as result_file:
    result_csv_reader = csv.reader(result_file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data = list(result_csv_reader)


with open('result.json', 'w') as f:
        json.dump(data, f, indent=4)
 
