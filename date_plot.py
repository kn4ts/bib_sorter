#!/usr/bin/python
#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import math

#ソートされたデータを受け取ってグラフを描画する
def graph_plot(date):

    year = [e.year for e in date]
    ID = [e.ID for e in date]
    title = [e.title e in date]
    keyword = [e.keyword e in date]

    plt.plot(year)
    plt.xticks([0,1,2],['M','E','I'])
    plt.show()
