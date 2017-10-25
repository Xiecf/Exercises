# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 00:03:05 2017

@author: xie
"""

import matplotlib.pyplot as plt

x = range(1,5001)
y = [a**3 for a in x]

plt.scatter(x,y,c=y,cmap=plt.cm.Blues,s=10)
plt.axis([0,5000,0,5000**3])
plt.title('1-5000sancifang',fontsize=24)     #设置标题、字号
plt.xlabel('x',fontsize=14)     #设置x轴标签、字号
plt.ylabel('y',fontsize=14)       #设置y轴标签、字号
plt.tick_params(axis='both',labelsize=14)       #设置刻度样式及字号 

#plt.show()
plt.savefig('1-5000sancifang.png',bbox_inches='tight')