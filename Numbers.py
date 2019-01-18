#!/usr/bin/env python
# coding: utf-8

# In[60]:


#Question:
#Write a program which will find all such numbers which are divisable by 7 but are not a multiple of 5, between 2000
#and 3200 (both included) 
#The numbers obtained should be printed in a comma-seperated sequence on a single line.
#%%run numbers

x = list(range(2000,3200))
counter=0
while True:
    if (counter>=len(x)):
        print ("end")
        break
    numberdisvisableby7 = x[counter]
    counter += 1
    if (numberdisvisableby7%7 == 0 and numberdisvisableby7%5 !=0):
        print(numberdisvisableby7,end=", ")
        
        
        
#print (x[0])




# In[ ]:





# In[ ]:





# In[ ]:




