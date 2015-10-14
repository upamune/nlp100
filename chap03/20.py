# coding: utf-8
import json

f = open('./jawiki-country.json', 'r')
w = open('./jawiki-country-uk.txt', 'w')

for line in f:
    record = json.loads(line)
    if record['title'] == "イギリス":
        w.write(record['text'])
