#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 列表生成式
# [exp foreach if]
# 万花筒

list1 = [x*x for x in range(1,11) ]
print list1

list2 = [x*x for x in range(1,11) if x%2==0]
print list2

# [1,2,3,4] * [1,2]
list3 = [x*y for x in range(1,5) for y in range(1,3)]
print list3

list4 = [k+'='+v for k,v in {'name':'yangzj','age':18}.iteritems() if isinstance(k,str) and isinstance(v,str)]
print list4

import os
dir_list = [d for d in os.listdir('.')]
print dir_list
