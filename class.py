#!/usr/bin/env python
# -*- coding: utf-8 -*-

'my first python class code.'

__author__='yangzj'

class SuperMan(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 别漏掉self
    def say_hello(self):
        print 'hi, my name is %s, %d years old.' % (self.name, self.age)

me = SuperMan('yangzj',18)
you = SuperMan('spider',28)

me.say_hello()
you.say_hello()

print dir(SuperMan)

class Spider(SuperMan):
    pass

test = Spider('test',11)
test.say_hello()