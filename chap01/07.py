# coding: utf-8

__author__ = 'upamune'


def xyz(x, y, z):
    str = "%s時の%sは%s" % (x, y, z)

    return str

if __name__ == '__main__':
    x = 12
    y = "気温"
    z = 22.4

    print(xyz(x, y, z))

