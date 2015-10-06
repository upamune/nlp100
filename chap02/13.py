# coding: utf-8
__author__ = 'upamune'


dat1 = open('./col1.txt')
dat2 = open('./col2.txt')

for d1, d2 in zip(dat1, dat2):
    str = "\t".join((d1.strip(), d2.strip()))
    print(str)
