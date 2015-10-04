import re
__author__ = 'upamune'

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# words =map(lambda x:len(x), re.sub(r'[,.]', '', str).lower().split(" "))

words = re.sub(r'[,.]', '', str).lower().split()

len_words = [len(w) for w in words]

print(len_words)
