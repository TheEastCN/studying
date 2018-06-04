# -*- coding:utf-8 -*-

def range2(n):
    count = 0
    while count < n:
        print(count)
        count += 1
        yield count

r = range2(5)

# next(r)
# next(r)




6187732