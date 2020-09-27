import linecache
# row = linecache.getline('amounts.csv', 282748)
# print(row)
#

import csv
import linecache
import timeit

def brute_search():
    with open('amounts.csv') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            if reader.line_num in [4, 41231, 284400]:
                rows.append(row)
        return rows

def cache_search():
    return list(csv.reader(linecache.getline('amounts.csv', i) for i in [4, 41231, 284400]))


print(timeit.timeit(brute_search))