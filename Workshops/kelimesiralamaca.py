# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 23:07:14 2021

@author: mrtke
"""

cumle=input('Cümlenizi giriniz: ')
cumle=cumle.split()
print(cumle)
cumle=sorted(cumle)
for i in range(len(cumle)):
    print(cumle[i])
    

