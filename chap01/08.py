__author__ = 'upamune'


def cipher(str):
    result = ""

    for x in str:
        if x.islower():
            result += chr(219 - ord(x))
        else:
            result += x

    return result


def decipher(str):
    result = ""

    for x in str:
        n = 219 - ord(x)
        c = chr(n) if 0 <= n and n <= 256 else chr(0)

        if c.islower():
            result += c
        else:
            result += x

    return result


if __name__ == '__main__':

    str = "My name is Dylan McKay."

    enc = cipher(str)
    dec = decipher(enc)

    print(enc)
    print(dec)


