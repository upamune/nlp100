# coding:utf-8

__author__ = 'upamune'


dat = open('./hightemp.txt', 'r')

f1 = open('./col1.txt', 'w')
f2 = open('./col2.txt', 'w')

for line in dat:
    col1, col2, *_ = line.split('\t')
    f1.write("%s\n" % (col1))
    f2.write("%s\n" % (col2))
