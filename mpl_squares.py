# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import matplotlib.pyplot as plt    #导入模块pyplot，并指定别名plt

input_values = [1,2,3,4,5]      #创建x轴列表
squares = [1,4,9,16,25]     #创建y轴列表

plt.plot(input_values,squares,linewidth=5)       #将x轴、y轴、线宽参数传入
plt.title('Square Numbers',fontsize=24)     #设置标题、字号
plt.xlabel('Value',fontsize=14)     #设置x轴标签、字号
plt.ylabel('Square of Value',fontsize=14)       #设置y轴标签、字号
plt.tick_params(axis='both',labelsize=14)       #设置刻度样式及字号 
             
plt.show()      #显示绘制的图形