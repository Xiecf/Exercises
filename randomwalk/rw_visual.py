#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'rw_visual.py'
__author__ = 'xiechaofan'
__mtime__ = '2017/12/31'
"""
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	# 创建一个RandomWalk实例,并将其包含的点都绘制出来
	rw = RandomWalk()
	rw.fill_walk()
	plt.scatter(rw.x_values, rw.y_values, s=5)
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)
	plt.show()

	keep_running = input("创建其他漫步?(y/n):")
	if keep_running == 'n':
		break
