# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:38:20 2019

@author: Lenovo
"""

import numpy as np
from scipy.stats import bernoulli
import seaborn as sns

class car ():
    
    
    def __init__(self):
        self.isCarBroken=0
 
    def dagilimGrafigiCizdir(array):
        ax = sns.distplot(array,
                 kde = False,
                 color = "orange",
                 hist_kws={"linewidth": 15, "alpha" : 1});

        ax.set(xlabel = "bernoulli", ylabel = "Frekans");

               
y=np.array([],dtype=object)


a=car()


for i in range (0,100):
    a=car()
    if(i%5==0):
        a.isCarBroken=1
    
    y = np.append(y,a.isCarBroken)          
    
    
    

car.dagilimGrafigiCizdir(y)    