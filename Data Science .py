#!/usr/bin/env python
# coding: utf-8

# # Python Codes Assignmnet Questions_List

# # Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

# In[2]:


lis1 = []
lis1 = [data for data in input("Enter the List Numbers: ")]
numbr=[]
for ele in lis1:
    if ele.strip():
        numbr.append(ele)
        
print(numbr)


# In[8]:


tup1=[]
tup1=input("Enter the Tuple Numbers: ")
numbr=[]
for ele in tup1:
    if ele.strip():
        numbr.append(ele)
print(numbr)


# # Write a Python program to display the first and last colors from the following list.
# 
# color_list = ["Red","Green","White" ,"Black"]

# In[ ]:


color_list = ["Red","Green","White" ,"Black"]
print("The Color in the list are: " + str(color_list)) 


# In[ ]:


Colur=[color_list[i] for i in (0,-1)]
print ("The first and last colors of this list: "+ str(Colur))


# # Write a Python program to print the even numbers from a given list.

# In[11]:



list1 =[40,21,1,3,6,9,5]
even_nos = [num for num in list1 if num % 2 == 0]
print("Even numbers in the list: ", even_nos)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




