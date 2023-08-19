# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:31:51 2023

@author: hamza
"""
# using monte carlo estimation to calculate probability that a coin with radius r land on a squar with length 1 
import numpy as np

def cointoss(r,s):
    
    x = np.random.uniform(size=s)
    y= np.random.uniform(size=s)
    count = 0  
    for i in range(s) :
        if x[i]  - r <0 or x[i]+r>1 or y[i]  - r <0 or y[i]+r>1 :
            count = count+1
    result = 1 - (count/s)        
    print(result)        
cointoss(0.1, 10000)         
