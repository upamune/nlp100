# coding: utf-8

import collections

__author__ = 'upamune'

if __name__ == '__main__':
    f = open('hightemp.txt', 'r')

    prefs = []

    for line in f:
        p = line.split("\t")[0]
        prefs.append(p)

    for item in collections.Counter(prefs).most_common():
        print "%s %s" % (item[0], item[1])
