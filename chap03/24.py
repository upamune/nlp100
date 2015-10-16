# encoding: utf-8

import re

f = open('./jawiki-country-uk.txt', 'r')

for line in f:
    reg = re.search(u'\[\[(File|ファイル):(.*?)\|.*?\]\]', line)
    if reg:
        print(reg.group(2))
