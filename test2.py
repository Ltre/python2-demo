#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

print '===================================='

list = [1,2,'a']
print list
print r"list.__len__()=", list.__len__()
print r"len(list)=", len(list)
print list[0]
print list[1]
print list[2]
#print list[3] #err code

print '===================================='

list.append('fdsffds')
list.append(489463)
list.append(list)
print 'after append:', list
print list[5][5][5][5][5][5][5][5][5][5][5][5]
print 'after append:', list
print r'递归后长度',len(list) #只算一层
list.pop()
print 'after pop():', list
list.pop(0)
print 'after pop(0):', list
print list[-1]

print '===================================='

tuple = (1,2,3)
print tuple
#tuple[0] = 'a' #err code
print tuple[0]
print tuple[-1]
tuple = (1) # 歧义！这不是一个元组
print tuple
tuple = (1, ) #对于只有一个元素的，需要加上逗号，以消除歧义
print tuple

print '===================================='

tuple = (1,2,3,4,5)
print r"tuple.__len__()=", tuple.__len__()
print r"len(tuple)=", len(tuple)

print '===================================='

tuple = (1,2, [1,2] )
print tuple
tuple[2][1] = 'a' # tuple里的list还是可以更改的
print tuple

print '===================================='


