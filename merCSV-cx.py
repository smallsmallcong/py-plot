#-*-coding:utf-8 -*-
#snow
#2020.7.3
#根据目标时段匹配数据

import pandas as pd
import numpy as np
import csv
import os,sys
import glob
from pandas.tseries.offsets import Day, Hour, Minute
import datetime
#reload(sys)
#sys.setdefaultencoding('utf-8')
filepath = r"D:\merCSV"
# filename = r"beijing.csv"
timepath = r"D:\merCSV\out"
time_name = r"timelist.csv"
# baoding = r"baoding.csv"

timefile = os.path.join(timepath, time_name)
time_list = pd.read_csv(timefile)
time_list["time"]= time_list["time"].apply(lambda x: str(x))

nameList = [nList for nList in os.listdir(filepath) if nList[-3:]=='csv']
for fileName in nameList:
    datafile = os.path.join(filepath, fileName)
    temData = pd.read_csv(datafile)
    temData["time"] =pd.to_datetime(temData["time"], format='%Y-%m-%d')
    temData["time"]= temData["time"].apply(lambda x: x.strftime('%Y%m%d'))
    fullData = pd.merge(time_list, temData, on=["time"], how='left')
    outfile = fileName[:-4]+'_full.csv'
    fullData.to_csv(outfile, index=False, encoding='utf_8')




