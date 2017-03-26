#! usr/bin/env python

import sys

def do_reduce(country, values):
    return country, sum(values)

prev_country = None
values = []

for line in sys.stdin:
    country, value = line.split("\t")
    if country != prev_country and prev_country is not None:
        result_country, result_value = do_reduce(prev_country, values)
        print(result_country + "\t" + str(result_value))
        values = []
    prev_country = country
    values.append(float(value))

if prev_country is not None:
    result_country, result_value = do_reduce(prev_country, values)
    print(result_country + "\t" + str(result_value))
