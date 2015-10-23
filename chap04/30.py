# -*- coding: utf-8 -*-
# https://github.com/himkt/nlp-100knock/blob/master/python/4/knock30.py


def knock30():

    sentense_morph_list = []
    morph_mapping_list = []

    for line in open('./neko.txt.mecab', 'r'):
        line = line.rstrip()

        if line == 'EOS':
            sentense_morph_list.append(morph_mapping_list)
            morph_mapping_list = []
            continue

        elements = line.split('\t')
        morph_info = elements[1].split(",")

        morph = {
            'surface': elements[0],
            'base': morph_info[6],
            'pos':  morph_info[0],
            'pos1': morph_info[1],
        }

        morph_mapping_list.append(morph)

    return sentense_morph_list

if __name__ == '__main__':

    sentense_morph_list = knock30()
    print(len(sentense_morph_list))
