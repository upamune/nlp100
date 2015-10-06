# coding: utf-8
__author__ = 'upamune'


if __name__ == '__main__':
    f = open('hightemp.txt', 'r')

    lines = []

    for line in f:
        col = line.split('\t')
        lines.append(col)

    sorted_lines = sorted(lines, key=lambda x: float(x[2]))

    for line in sorted_lines:
        print("\t".join(line))
