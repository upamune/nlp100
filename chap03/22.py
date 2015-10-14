# encoding: utf-8

import re

f = open('./jawiki-country-uk.txt')

for line in f:
    reg = re.search("\[\[Category:(.*?)\]\]", line)

    if reg:
        print(reg.group(1))
