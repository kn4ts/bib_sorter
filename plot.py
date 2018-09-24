import numpy as np
import matplotlib.pyplot as plt

# データ（リストの配列)の個数を数える クラスのリストが来る
n = len(paper_list)

#x_list y_list の空集合を定義
x_list = []
y_list = []
id_list = []

#organizeを数字に変換する関数を作成 M = 1 E = 2 I = 3 else = 0
def trans(x):
    if x == "M":
        return 1
    elif x == "E":
        return 2
    elif x == "I":
        return 3
    else:
        return 0

# paper_listのorganizeメソッドを数値に変換
for i in range(n):
    x_list.append(trans(paper_list.method_orgnaize[i]))

# paper_listのyearメソッドをy_listに格納
for i in range(n):
    y_list.append(paper_list.method_year[i]))

# paper_listのIDメソッドをid_listに格納
for i in range(n):
    id_list.append(paper_list.method_id[i]))

#描画
plt.xticks([0,1,2,3],["others","M","E","I"])
for (i,j,k) in zip(x_list,y_list,id_list):
    plt.plot(i,j "o")
    plt.annotate(k, xy=(i, j))
plt.show()
