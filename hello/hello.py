""" msg = 'Hello World'
g = lambda x, y: str(x) + str(y)
print (g('aaa','bbb'))

def aaa(x):
    return x % 2
temp = range(10)
show = filter(aaa, temp)
list(show)

list(filter(lambda x : x % 2, range(10)))
list(map(lambda x: x%3, range(20))) """


def test(a, b):
    if b <= 10:
        c = a * b
        a = a + 1
        b = b + 1
        return c


print(test(1, 3))
