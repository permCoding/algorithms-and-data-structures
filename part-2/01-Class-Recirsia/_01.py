#!/usr/bin/python3
# -*- coding: utf-8 -*-


# ((1* 2 + 1)* 2 + 0)* 2 + 1 = 13
# 11 0 1

def to_dec_rec(b):
   if b == '':
      return 0
   else:
      return to_dec_rec(b[:-1])*2 + int(b[-1])

def to_dec(b):
   d = 0
   for i in range(len(b)):
      d += int(b[i]) * 2** (len(b)-1-i)  
   return d

b = str(input())
print(to_dec(b))
print(to_dec_rec(b))