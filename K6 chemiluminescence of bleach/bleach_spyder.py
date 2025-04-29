# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:29:11 2024

@author: mvanstav
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import glob
import os.path

# dataX_raw, dataY_raw = np.loadtxt("bleach/A_CL_T2.csv", skiprows = 21, usecols = (2, 3), delimiter = ',', unpack = True)

# fig = plt.figure(1)
# ax = fig.subplots()

# goodfit = "n"
# i = 0

# while(goodfit =='n'):
#     #index = int(input("index? "))
#     #fig.clf()
#     #ax.plot(dataX_raw, dataY_raw)
#     #ax.plot(dataX_raw[index:], dataY_raw[index:])
#     i = i + .2
#     ax.plot(dataX_raw, dataY_raw+i)
#     ax.figure.canvas.draw_idle()
#     goodfit = input("is the trim good? ")
    
# print("awesome!")

# plt.clf()
# i = 0
# x = np.linspace(0, 10, 100)
# y = x**2
# while(i<10):
#     plt.clf()
#     plt.plot(x, y)
#     plt.plot(x, y+i)
#     i = i + 1
#     thing  = int(input("question? "))
#     print(f'i is {i}')
#     plt.pause(.1)

fig = plt.figure(1)
ax = fig.subplots()

i = 0
x = np.linspace(0, 10, 100)
y = x**2
while(i<10):
    fig.clf()
    ax = fig.subplots()
    ax.plot(x, y)
    ax.plot(x, y+i)
    i = i + 1
    thing = int(input("question? "))
    plt.pause(.1)
