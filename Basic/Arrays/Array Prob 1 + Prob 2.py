#!/usr/bin/env python
# coding: utf-8

# In[8]:


def rotLeft(a, d): 
    
    j=0
    b =a.copy()
    l = len(a)
    
    for i in range(d,l):
        
        b[j] = a[i]
       
        j+=1
    
    for i in range (0,d): 
        
        b[j] = a[i]
        j+=1
        
    return b


# In[9]:


x=[1,2,3,4,5]


# In[12]:


print(rotLeft(x,4))


# In[18]:


def reverseArr(x):
    rev=[]
    temp=x
    for i in range(len(x)):
        temp = rotLeft(temp, len(temp) - 1)
        output.append(temp[0])
        temp.pop(0)
    return output


# In[19]:


print(reverseArr(x))


# In[ ]:





# In[ ]:




