#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hello

hello.whatever()


# from module_a import utils
# utils.test()

# error code~
# import module_a
# module_a.utils.test()


# from module_a import test_class
# test = test_class.SuperMan('holy shit',18)
# test.say_hello()
from module_a.test_class import SuperMan
test = SuperMan('fda',123)
test.say_hello()


