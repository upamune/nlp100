# coding: utf-8
__author__ = 'upamune'


if __name__ == '__main__':
    f = open('./hightemp.txt', 'r')

    prefs = set()

    for line in f:
        col1 = line.split('\t')[0]
        prefs.add(col1)

    for pref in prefs:
        print(pref)

