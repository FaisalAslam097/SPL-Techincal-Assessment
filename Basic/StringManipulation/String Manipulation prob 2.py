#!/usr/bin/env python
# coding: utf-8

# In[96]:


s ='We Are Your Technology Partners'
def char_remover(str1,char):
    
    ch=char
    filt=""
    for i in str1:
        if(i!=ch):
            filt=filt+i
    return filt    
print(char_remover(s,' '))


# In[ ]:




