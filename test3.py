#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

print '===================================='

if 1 > 2:
    print 'fuck'
else:
    print 'nima'

print '===================================='

if 1 > 2:
    print 'fuck'
    print 'fuck'
    print 'fuck'
else:
    print 'nima'
    print 'nima'
    print 'nima'

print '===================================='

if 1 > 2:
    print 'fuck'
elif 1 == 1:
    print 'wocao'
else:
    print 'nima'

print '===================================='

list = [2,3,4,5,6,7,8]
for l in list:
    print l

print '===================================='

sum = 0 # notice: sum() is also a function
list = [2,3,4,5,6,7,8]
for i in list:
    sum += i
print sum

print '===================================='

print range(5)
print range(6,10)
print range(1,100,10)
print range(1,101,10)
print range(1,102,10)

print '===================================='

name = raw_input('your name:')
print name
print int(name) # 若输入非整数，则报错

print '===================================='