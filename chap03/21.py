# encoding: utf-8

import re

f = open('./jawiki-country-uk.txt', 'r')

for line in f:
    if re.search("Category", line):
        print(line)
