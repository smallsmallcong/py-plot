#!/usr/bin/python
import pandas as pd
import numpy as np
import os
# import matplotlib
import matplotlib.pyplot as plt
# import matplotlib.mlab as ml
from matplotlib import colors, ticker, cm
# import re
from matplotlib.colors import LinearSegmentedColormap, from_levels_and_colors
# from math import *
# from matplotlib.backends.backend_pdf import PdfPages

# filepath = r"D:\merCSV\out"
# # filename = r"BTHS_pm25.csv"
# # datafile = os.path.join(filepath, filename)

# sphinx_gallery_thumbnail_number = 2
#bounds = [0.01,0.1,0.3,0.5,1,3,5,10,20,30,40,50,60,70]
#cmap, norm = from_levels_and_colors(bounds,['navy','blue','deepskyblue', 'skyblue','green', 'limegreen', 'yellow','orang    e','r', 'darkred','darkviolet','magenta','indigo'])
#
# plot_data = pd.read_csv(datafile,usecols = [1,2,3,4,5,6,7,8,9,10])
# temData = plot_data[450:500]
# print(temData)
# data_matri = np.array(temData)
#figsize = [8,6]
# fig = plt.figure()
# plt.rcParams['figure.figsize']=(10, 15)
# ax = fig.add_subplot(111)

fig, ax = plt.subplots(figsize = [10,10])
# bounds = [0,75,150,225,300,450,600]
# cmap, norm = from_levels_and_colors(bounds,['green','yellow','orange','r','darkviolet','maroon'])
# im = ax.imshow(data_matri,cmap=cmap,norm = norm)

# cax = ax.pcolor((data_matri,cmap=cmap, norm = norm)
# We want to show all ticks...
#ax.set_xticks(np.arange(len(farmers)))
#ax.set_yticks(np.arange(len(vegetables)))

# ... and label them with the respective list entries
#ax.set_xticklabels(farmers)
#ax.set_yticklabels(vegetables)

# Rotate the tick labels and set their alignment.
#plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
 #        rotation_mode="anchor")
ax.set_title("BTHS daily $PM_{2.5}$ (ug/$m^{3}$)")
#ax.set_aspect(5)

# fig.tight_layout()
# fig.set_size_inches(10,10)
plt.savefig('BTHS-PM25-4.png')
# plt.show()
