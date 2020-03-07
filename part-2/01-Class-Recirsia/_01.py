#!/usr/bin/python3
# -*- coding: utf-8 -*-

from _module import Convert

obj1 = Convert('11000')
obj2 = Convert(17)
obj3 = Convert()

lst = [obj1, obj2, obj3]

for item in lst:
   print(item)


