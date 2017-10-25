# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:22:18 2017

@author: xie
"""

def zimu(x):
    biaoji = True
    n = len(x)
    while biaoji and n > 1:
        if x[0] == x[n]:
            del x[0]
            del x[n]
        else:
            biaoji = False




zimu('acbca')
