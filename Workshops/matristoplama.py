# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:45:55 2021

@author: mrtke
"""

x=[[1,3,5],[2,4,1],[1,5,7]]
y=[[3,3,4],[2,4,1],[3,5,4]]
z=[[0,0,0],[0,0,0],[0,0,0]]
z[0][0]=x[0][0]+y[0][0]
z[0][1]=x[0][1]+y[0][1]
z[0][2]=x[0][2]+y[0][2]
z[1][0]=x[1][0]+y[1][0]
z[1][1]=x[1][1]+y[1][1]
z[1][2]=x[1][2]+y[1][2]
z[2][0]=x[2][0]+y[2][0]
z[2][1]=x[2][1]+y[2][1]
z[2][2]=x[2][2]+y[2][2]
print(z)
