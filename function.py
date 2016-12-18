#!/usr/bin/env python
# -*- coding: utf-8 -*-

def funcname(parameter_list):
    pass

def funcname(self, parameter_list):
    raise NotImplementedError

def funcname(self, parameter_list):
    pass

@staticmethod
def funcname(parameter_list):
    pass

def nop():
    pass


def how_old_are_you(age):
    # 1.类型检查
    if not isinstance(age,(int,float)):
        raise TypeError("how_old_are_you: Type error.")
    # 2.逻辑判断
    greeting = 'Hi,'
    if age<=18 and age>0:
        return greeting+'boy.',age
    elif age>18 and age<=100:
        return greeting+'man.',age
    else:
        return

# age = 10
# age = 19
# age = 110 
age = int('19')
# age = 'A'
greeting,age = how_old_are_you(age)
if greeting==None:
    greeting = 'are you kidding me?'
print greeting,'You are '+str(age) 

# 变长参数
def calc(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number * number
    return sum

print calc(1,2,3)

# nums = [1,2,3]
nums = (1,2,3)
print calc(*nums)

# 注意顺序：必选 then 默认 then 变长 then 键值对
def func_demo(a,b,c=0,*args,**map):
    pass

# python通用函数声明
def func_common(*args,**map):
    pass

