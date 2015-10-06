# coding: utf-8
__author__ = 'upamune'


def head(f, n):
    for idx, line in enumerate(f):
        if(int(n) == idx):
            return
        print(line)

if __name__ == '__main__':
    f = open('./hightemp.txt', 'r')
    n = input()

    head(f, n)
