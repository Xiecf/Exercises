# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:20:34 2017

@author: xie
"""

import matplotlib.pyplot as plt

a =range(1,1001)
b = [x**2 for x in a]

plt.scatter(a,b,c='r',s=20)
plt.axis([0,1100,0,1100000])    #设置每个坐标轴的取值范围
plt.title('Square Numbers',fontsize=24)     #设置标题、字号
plt.xlabel('Value',fontsize=14)     #设置x轴标签、字号
plt.ylabel('Square of Value',fontsize=14)       #设置y轴标签、字号
plt.tick_params(axis='both',labelsize=14)       #设置刻度样式及字号 
#plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')

