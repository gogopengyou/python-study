#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 首先明确一点，生成器是一个可迭代对象
# 它比list要节省空间，因为每一个元素都是由一轮推算得出，并非一开始就占有内存
# 它比列表生成式要更强大，因为它的万花筒表达式可以是一个函数(通过yield关键字)

g1 = (x*x for x in range(1,5))
print g1
for x in g1:
    print x

def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        print b
        a,b=b,a+b
        n=n+1
fib(6)

# yield func-->gen
def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1

g2 = fib(6)
print g2

for x in g2:
    print x 