def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


print(xo("xoxo"))
print(xo("xoo"))