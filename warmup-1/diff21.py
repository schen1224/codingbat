def diff21(n):
    if n > 21:
        return abs(n-21) * 2
    return abs(n-21)


print(diff21(19))
print(diff21(10))
print(diff21(21))
