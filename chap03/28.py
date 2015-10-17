# encoding: utf-8

import re


def rm_link(line):

    reg = re.search('\[\[(.*?)\]\]', line)

    if not reg:
        return line

    link = reg.group(1)

    reg = re.search('(.*?)\|(.*?)', link)

    if reg:
        return reg.group(1)
    else:
        return link


def rm_comment(line):
    reg = ('<!--\s(.*?)\s-->', line)

    if reg:
        return reg.group(1)
    else:
        return line


def rm_stub(line):
    reg = re.search('{{(.*?)}}', line)

    if reg:
        return reg.group(1)
    else:
        return line


def rm_markup(line):
    line = rm_link(line)
    line = rm_comment(line)
    line = rm_stub(line)

    return line

f = open('./jawiki-country-uk.txt', 'r')

flag = False

basic_info = "\n"

for line in f:
    line = line.replace('\'', '')
    line = rm_markup(line)

    if flag and re.search('^}}', line):
        break

    if flag:
        basic_info += line

    if re.search(u'基礎情報', line):
        flag = True

basic_info_arr = basic_info.split('\n|')
basic_info_dic = {}

for v in basic_info_arr:
    items = v.split('=')
    if len(items) == 2:
        key = items[0].strip()
        val = items[1].strip()
        basic_info_dic[key] = val

for key, val in basic_info_dic.items():
    print("%s = %s" % (key, val))
