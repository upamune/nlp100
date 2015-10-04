# coding: utf-8

__author__ = 'upamune'


def n_gram(n, mode, string):
    if mode == 'char':
        feature_list = [char for char in string.replace(' ', '')]
    else:
        feature_list = string.split()

    n_gram_list = []

    if len(feature_list) > n:
        for i in xrange(len(feature_list) - n + 1):
            n_gram_list.append("".join(feature_list[i: i + n]))

    return n_gram_list


if __name__ == '__main__':
    n = 2

    str = "I am an NLPer"

    print(n_gram(n, 'word', str))
    print(n_gram(n, 'char', str))
