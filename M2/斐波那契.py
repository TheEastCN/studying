# -*- coding:utf-8 -*-


def fib_seq(n):

    if n == 0 or n == 1:
        return 1

    else:
        return fib_seq(n - 1) + fib_seq(n - 2)


a = fib_seq(8)
print(a)
