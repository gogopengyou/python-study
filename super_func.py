#!/usr/bin/env python
# -*- coding: utf-8 -*-

def funcname(x):
    if isinstance(x,int):
        return x*2
    return

test = funcname
print test
print test(10)

def funcname2(x,test):
    return test(x)

print funcname2(10,test)


print map(funcname,[1,2,3,4,5])

def reduce_func(x,y):
    return x+y
print reduce(reduce_func,[1,2,3,4,5])

print reduce(reduce_func,map(funcname,[1,2,3,4,5]))


