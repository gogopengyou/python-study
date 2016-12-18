#!/usr/bin/env python
# -*- coding: utf-8 -*-

for x in range(5):
    print x

n = 5
while n>0:
    n = n - 1
    print n

temp = '2000'
if int(temp)<2016:
    print 'cast type'

# while n<1:
#     print ':('

map = {'Yao':11,'Jodan':23,'Kobe':24}
print map['Yao']
print map.get('Yao')
print map.get('wade')

if map.get('wade')==None:
    print 'wade\'s number is none'


s = set([1,1,3,3,4,4])
print s

map2 = {"name":"yangzj","age":18}
for key in map2:
    print key

for value in map2.itervalues():
    print value

for key,value in map2.iteritems():
    print key,value 

for ch in 'ABCD':
    print ch 

from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)

for i,val in enumerate('abc'):
    print i,val

