#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

print '===================================='
print u'中国'
print 'abc'.decode('utf-8')
print u'中文'.encode('gbk')
print '===================================='
print r"'fdsafd'.__len__()=", 'fdsafd'.__len__()
print r"len('fdsafd1111')=", len('fdsafd1111')
print r"len(u'abc')=", len(u'abc')
print r"len(u'尼玛')=", len(u'尼玛')
print r"len('尼玛')=", len('尼玛')
print r"r'卧槽'=", r'卧槽'
print '===================================='
print 'Hi %s, you are shabi', 'WANGNIMA'
print "Hi %s, you are sillyB", 'ZHANGQUANDAN'
print "Hi %s, hehe" %'gun'
print '%s, you have %d coins'%('NIMABI', 99)
print '===================================='
print u'大概有%f%%的人没睡'%(50)
print u'大概有%.2f%%的人没睡'%(50)
print u'大概有%.0f%%的人没睡'%(50)
print r'大概有%.0f%%的人没睡'%(50)
#print r'大概有%.0f%的人没睡'%(50) #err code
print '===================================='

