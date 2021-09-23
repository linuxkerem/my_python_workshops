# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:44:02 2021

@author: mrtke
"""

ogrenciler=["Engin",'Derin','Salih','Ali','Ayşe']
filetopappend=open('ogrenciler.txt','a')
for l in ogrenciler:
    filetopappend.write(l)
    filetopappend.write('\n')
filetopappend.close()