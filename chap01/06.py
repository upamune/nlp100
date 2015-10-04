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

    str1 = "paraparaparadise"
    str2 = "paragraph"

    x = set(n_gram(n, "char", str1))
    y = set(n_gram(n, "char", str2))

    # sum
    sum = x.union(y)
    print(sum)

    # diff
    diff1 = x.difference(y)
    diff2 = y.difference(x)
    print(diff1)
    print(diff2)

    # common
    common = x.intersection(y)
    print(common)

    # isInclude
    se = "se"
    print(se in x)
    print(se in y)

