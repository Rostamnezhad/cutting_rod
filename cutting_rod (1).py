#!/usr/bin/env python
# coding: utf-8

# In[1]:



def cut_rod(price, length):
    value = [0 for n in range(length+1)]
    value[0] = 0
    
    for i in range(1, length+1):
        max_value = -32000
        
        for j in range(i):
            max_value = max(max_value, price[j] + value[i-j-1])
        value[i] = max_value
        
    return value[length]   
        
    
#main code
n = int(input(""))
test_arr = list(map(int,input("").strip().split()))[:n]
size = len(test_arr)
print(str(cut_rod(test_arr, size)))


# In[ ]:





# In[ ]:




