__author__ = 'upamune'

words = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".replace('.', '').lower().split()

match_number = [n-1 for n in (1, 5, 6, 7, 8, 9, 15, 16, 19)]

result = []

for idx, w in enumerate(words):
    i = idx + 1
    result.append((w[0], i) if idx in match_number else (w[0:2], i))

print(result)

