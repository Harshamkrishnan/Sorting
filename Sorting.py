#!/usr/bin/env python
# coding: utf-8

# In[17]:


n = input("How many elements to be added:")
input_string = input("Enter the Elements to be added seperated by a comma:")
input_list = input_string.split(",")
list = []
for i in input_list:
        list.append(int(i))
print(list)
list.sort()
print(list)


# In[20]:


list = []
n = int(input("How many elements to be added:"))
for i in range(0,n):
    print("Enter the element to be added at the index", i, )
    item = int(input())
    list.append(item)
print(list)
list.sort()
print("list after sorting", list)


# In[1]:





# In[11]:


def BubbleSort(n,l):
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]               
l = []
n = int(input("How many elements to be added:"))
for i in range(0,n):
    print("Enter the element to be added at the index", i, )
    item = int(input())
    l.append(item)
print("List before sorting :", l )
BubbleSort(n,l)
print("List after sorting :", l )


# In[ ]:





# In[ ]:




