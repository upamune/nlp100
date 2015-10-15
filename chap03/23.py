# encoding: utf-8

import re

f = open('./jawiki-country-uk.txt', 'r')

for line in f:
    reg = re.search('^(=+)(.*?)(=+)', line)
    if reg:
        print(len(reg.group(1)), reg.group(2))
