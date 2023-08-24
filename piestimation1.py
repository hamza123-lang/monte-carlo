# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:39:00 2023

@author: hamza
"""

import numpy as np 
def estimationpi(it=100000):
    
    x = np.random.uniform(-1,1,it)
    y=np.random.uniform(-1,1,it)
    result = 0
    for i in range(len(x)):
        if  ((x[i])**2 + (y[i])**2 )<1 :
            result +=1
    final = (result/it )*4
    print(final)       
estimationpi()