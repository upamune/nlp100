# coding: utf-8

__author__ = 'upamune'



def tail(f, n):
    list = f.read().rstrip().split('\n')
    lines = list[-int(n):]

    for line in lines:
        print(line)

    return

if __name__ == '__main__':
    f = open('./hightemp.txt', 'r')
    n = input()

    tail(f, n)

