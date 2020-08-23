import matplotlib.pyplot as plt
import matplotlib.mlab as ml
from matplotlib import colors, ticker, cm
import pandas as pd
import re
import os
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, from_levels_and_colors
from math import *
from matplotlib.backends.backend_pdf import PdfPages

##绘制污染日历图

filepath = r"D:\merCSV\out"
filename = r"BTHS_pm25.csv"
datafile = os.path.join(filepath, filename)
font_size = 20
font_weight = 'normal'
ifile = pd.read_csv(datafile)

x = ifile['Days']
y = ifile.columns[2:]
zmatrix = np.zeros((len(y),len(x)))

for i in range(len(x)):
    for j in range(len(y)):
        zmatrix[j][i] =  ifile.at[i,y[j]]

X, Y = np.meshgrid(y, x)
bounds = [0,35,75,115,150,250,600]
cmap, norm = from_levels_and_colors(bounds,['limegreen','yellow','orange','r','purple','maroon'])
fig, ax = plt.subplots(figsize=[50, 18], ncols=1, nrows=1)
# cax = ax.pcolormesh(zmatrix, shading = 'gouraud', snap = 'True',cmap = cmap, norm=norm) #BTHS_matri2.pdf

cax = ax.pcolor(zmatrix, cmap = cmap, norm=norm) #不能修改shading方式
# cax = ax.imshow(zmatrix, interpolation="nearest",cmap = cmap, norm=norm)  #只适合len(x),len(y)相差不大的情况

cbar = fig.colorbar(cax, ax=ax, pad = 0.01, ticks = bounds)
# cbar.make_axes(fraction= 0.5,aspect = 20)

font1 = {'family': 'Times New Roman','weight': 'normal','size': 25,}  #图例的字体设置,prop参数适用于plt.legend

cbar.ax.tick_params(labelsize=22)

cbar.set_label('BTH ${PM2.5 ug/m^3}$',fontdict=font1) #添加上标：^ 添加下标：_ 斜体：$

y_tick = np.linspace(0.5,54.5,55) #生成固定间隔的列表
ax.yaxis.set_ticks(y_tick)
ax.set_yticklabels(y,size = 15)
ax.set_xlim([0,len(x)])
ax.set_ylim([0,len(y)])

x_tic = range(14,2191,91)  #每隔91天，即3个月，标一个刻度
# x_tic = [14,105,196,287,378,469,560,651,742,833,924,1015,1106,1197,1288,1379,1470,1561,1652,1743,1834,1925,2016,2107]
ax.xaxis.set_ticks(x_tic)
x_label = list()
for n in x_tic:
    x_label.append(x[n])
ax.set_xticklabels(x_label,size = 15)

x_lin = [364,729,1094,1460,1825]
for m in x_lin:
    x_line = [m]*55
    plt.plot(x_line,y,"deepskyblue", linewidth=3.0) #不同年的分割线 linestyle='--'

#设置坐标轴粗细
ax=plt.gca()
width_x = 3.0
ax.spines['bottom'].set_linewidth(width_x)#设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(width_x)#设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(width_x)#设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(width_x)#设置上边坐标轴的粗细

fig.savefig('BTHS_matri-12.jpeg',bbox_inches='tight')
