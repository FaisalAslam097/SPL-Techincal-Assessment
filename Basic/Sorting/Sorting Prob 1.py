#!/usr/bin/env python
# coding: utf-8

# In[88]:


Arr=[2,3,4,5,0,-1,-2,-3,-4]
def DistributeArray(a,b):
    output = []
    for i in a:
        if i < b:
            output.append(i)
    output.append(b)
    for i in a:
        if i > b:
            output.append(i)
    return output

print(DistributeArray(Arr,0))
print("In case of even numbers, pivot can be either of the two.")


# In[ ]:




