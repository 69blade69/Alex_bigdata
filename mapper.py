#! usr/bin/env python

import sys

def main(log):
#    data = log.replace(',', '').split(' ')
#    data = log.split(' ')
    data = log.split(',')
    yield data[2].strip(), data[4].strip()
#    yield data[2], data[4]

for line in sys.stdin:
    for country, value in main(line):
        print '%s\t%s' % (country, value)
