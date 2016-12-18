#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python强大的分片操作
# [startIndex:endIndex:step]
# 1.前闭后开 2.取尾留白

# 分片范围：list tuple str

list1 = [1,2,3,4,5,6,7,8,9]
print list1[0:3]
print list1[:3]
print list1[-3:]
print list1[-3:-1]
print list1[:]
print list1[::2]

str = '123456789'
print str[0:3]
print str[:3]
print str[-3:]
print str[-3:-1]
print str[:]
print str[::2]



