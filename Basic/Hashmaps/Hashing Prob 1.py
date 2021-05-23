#!/usr/bin/env python
# coding: utf-8

# In[80]:


x='abcd'
y='cdef'
def shareSubString(a,b):
    result = 0
    str1 = {}
    str2 = {}
    for i in a:
        if( i not in str2):
            str1[i] = len(str2)+1
    
    for i in b:
        if( i in str1):
            str2[i]= str1[i]
            result = 1
       
    return result

print(shareSubString(x,y))

