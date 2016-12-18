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

