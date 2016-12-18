#!/usr/bin/env python
# -*- coding: utf-8 -*-

list = ['element1','element2','element3']

# last element
print list 
print list[len(list)-1]
print list[-1]
print list[0]

print list.append('temp')
print list 
print list.insert(1,'temp2')
print list
print list.pop()

# 可容纳多种类型，所谓动态语言~
list2 = [123,'123',1.23,True,[4,5]]
print list2[-1][0]

# 不可变有序集合~
tuple = ('123','456','789')
print tuple[0]

