# coding: utf-8

__author__ = 'upamune'

s1 = u"パトカー"
s2 = u"タクシー"

str = "".join([ i + j for i, j in zip(s1, s2)])

print(str)
