#!/usr/bin/python
#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from operator import attrgetter
import re

def parser():

    paper_list = []
    temp ={}

    bibfile = open('./reference.bib','r')
    # bibfile = open('./anarticle.bib','r')

    # num_of_art=

    for line in bibfile:
    #     char_list = line.split('=')
        char_list = [ x.strip('@{ "",\n') for x in re.split('[{=]',line)]
        if line[0]=='@':
            temp.clear()
            # print('aaaaaaaaaaaaaaaaaaaaaaaaa')
        else:
            if char_list[0]=='inproceedings':
                # print('AAAAAAAAAAAAAAAAAAAAAAAAAAA')
                temp["ID"] = char_list[1]
            elif char_list[0]=='title':
                temp["title"] = char_list[1]
            elif char_list[0]=='year':
                temp["year"] = char_list[1]
            elif char_list[0]=='author':
                temp["author"] = char_list[1]
            elif char_list[0]=='keyword':
                temp["keyword"] = char_list[1]
            # print(temp)
            # print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')

        if line[0]=='}':
            paper_list.append(temp.copy())

        # print(line[0])            
        # print(char_list)
        # print(line.strip())
        # print(temp)
    bibfile.close()
#    print(paper_list)
#    print(len(paper_list))

    return paper_list

class Paper:    #論文クラス
    def __init__(self,title,year,author,keyword):
        self.ID = title
        self.year = int(year)
        self.keyword = keyword
        self.author = author
        #self.ID = ID

def main():  #論文リストを受け取る

    paper = parser()
    print(paper)
    paper_list = []
    
    for i in range(len(paper)):
        title = paper[i]['title']
        year = paper[i]['year']
        keyword = paper[i]['keyword']
        author = paper[i]['author']
        #ID = paper[i]['ID']
        paper_list.append(Paper(title,year,author,keyword))

    paper_list = sorted(paper_list, key=attrgetter('year'))

    #グラフの描画

    year = []
    ID = []
    title = []
    keyword = []

    for e in paper_list:
        year.append(e.year)
        #title.append(e.title)
        ID.append(e.ID)
        if e.keyword=='M':
            e.keyword = 0
            keyword.append(e.keyword)
        elif e.keyword=='E':
            e.keyword = 1
            keyword.append(e.keyword)
        elif e.keyword=='I':
            e.keyword = 2
            keyword.append(e.keyword)

    for(i,j,k) in zip(keyword,year,ID):
        plt.scatter(i,j)
        plt.xticks([0,1,2],['M','E','I'])
        plt.annotate(k,xy=(i,j))

    plt.show()

    #return paper_list

if __name__=='__main__':
    main()

