#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

print '===================================='

dict = {'w':111, 'a':'ttt', '123':56}
print dict
print dict['w']
#print dict[0] # err code
#dict.abc = 1 # err code
dict['abc'] = 1
print dict

print '===================================='

list = [1,2,3,4,5,6]
print 3 in list
dict = {'w':111, 'a':'ttt', '123':56}
print 'w' in dict # True ， in 关键字用来判断key是否存在
print '111' in dict # False
print 111 in dict # False

print '===================================='

dict = {'w':111, 'a':'ttt', '123':56}
print dict.get(111) # None
print dict.get('111') # None
print dict.get('w') # 111
#dict.pop() # err code 不指定参数会报错
#dict.pop(0) # err code 指定的键不存在也会报错
dict.pop('w')
print dict

print '===================================='

list = [1,2,3,4,5,5,6,6,6,7]
print list
#list.add('fuck') don't use add() before set()
list.sort()
print list
list = set(list)
print list
list.add(999)
print list
list.remove(3) # 参数指定的是元素的值
print list

print '===================================='

print '===================================='

print '===================================='

print '===================================='

print '===================================='

print '===================================='
