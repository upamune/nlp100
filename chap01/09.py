import random

__author__ = 'upamune'


def shuffle(word):
    result = "".join(random.sample(word, len(word)))

    return result


def typoglycemia(word):
    if len(word) <= 4:
        return word

    result = word[0] + shuffle(word[1:-1]) + word[-1]

    return result


if __name__ == '__main__':

    words = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .".split()

    result = " ".join([typoglycemia(w) for w in words])

    print(result)
