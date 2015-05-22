#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

print '===================================='

print cmp(1,2)
print cmp(2,1)
#print unicode('尼玛') # err code
print unicode(u'尼玛')

print '===================================='

aaa = abs
print abs(-2)
print aaa(-1)

print '===================================='

def shabi(x):
    print x
shabi(1)

print '===================================='

def nop():
    pass
nop()

def nop(): #函数可以重新定义
    if 1 == 1:
        print 'will pass'
        pass
nop()

print '===================================='

tuple = (1, 2.3)
def checkT(t):
    if not isinstance(t, (int, float)):
        return False
    else:
        return True
print checkT(tuple)

print '===================================='


print '===================================='


print '===================================='


print '===================================='


print '===================================='


