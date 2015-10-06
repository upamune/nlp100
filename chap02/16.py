# coding: utf-8

__author__ = 'upamune'

_marker = object()


def create_filenames(file_name, cnt):
    return ["%s_%d" % (file_name, x+1) for x in range(cnt)]

def file_split(f, n):
    lines = f.read().rstrip().split('\n')
    num = len(lines) // int(n)
    splited_files = [lines[i: i + num] for i in range(0, len(lines), num)]
    file_names = create_filenames("split_file", int(n))

    for x in range(int(n)):
        file_name = file_names[x]
        splited_file = splited_files[x]

        f = open(file_name, 'w')

        for file in splited_files:
            for line in file:
                f.write(line+"\n")


if __name__ == '__main__':
    f = open('./hightemp.txt', 'r')
    n = input()

    file_split(f,n)


