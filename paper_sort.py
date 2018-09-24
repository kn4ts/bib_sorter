#!/usr/bin/python
#coding:utf-8
import numpy as np
import math
from operator import attrgetter

class Paper:    #論文クラス
    def __init__(self,title,year,author,keyword,ID):
        self.title = title
        self.year = int(year)
        self.keyword = keyword
        self.author = author
        self.ID = ID



def main(paper):  #論文リストを受け取る

    paper_list = []
    
    for i in range(len(paper)):
        title = paper[i]['title']
        year = paper[i]['year']
        keyword = paper[i]['keyword']
        author = paper[i]['author']
        ID = paper[i]['ID']
        paper_list.append(Paper(title,year,author,keyword,ID))

    paper_list = sorted(paper_list, key=attrgetter('year'))

    return paper_list
   
if __name__ == '__main__':     #テスト

    paper = [{'title':'A','year':6,'author':'kuso','keyword':'M','ID':'ID'},
            {'title':'B','year':8,'author':'hoge','keyword':'I','ID':'ID'},
            {'title':'C','year':3,'author':'yamamoto','keyword':'E','ID':'ID'},
            {'title':'D','year':9,'author':'suzuki','keyword':'M','ID':'ID'},
            {'title':'E','year':2,'author':'murata','keyword':'E','ID':'ID'},
            {'title':'F','year':1,'author':'tamura','keyword':'I','ID':'ID'}]

    a = main(paper)

    year_ls = []

    print(a)
    for i in a:
        print(i.year)

