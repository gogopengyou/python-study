#!/usr/bin/env python
# -*- coding: utf-8 -*-

'This\'s document comment. hello.py '

__author__ = 'yangzj'

import sys

print sys.argv

def whatever():
    arg_list = sys.argv
    args_length = len(arg_list)
    if args_length==1:
        print arg_list[0]
    elif args_length==2:
        print arg_list[1]
    else:
        print 'too many arguments~'

if __name__=='__main__':
    whatever()
