#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python I/O demo'

__author__ = 'yangzj'

# f = open('/python27/readme.txt','r')
# print f.read()
# f.close()

# try:
#     file_name = '/python27/readme.txt'
#     f = open(file_name,'r')
#     print f.read()
# except IOError as e:
#     print e,file_name
# finally:
#     f.close()

# auto closed
with open('/python27/readme.txt','r') as f:
    print f.read()

