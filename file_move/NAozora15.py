#青空文庫作品データaozora_hackから利用したい作品データを絞り込み、まとめるプログラム
#旧字・旧仮名と新字・新仮名のグループの表から、作品番号を読み込む。
import pandas as pd
import csv
names=['人物ID',	'著者名',	'作品ID',	'作品名',	'仮名遣い種別',	'翻訳者名等',	'入力者名',	'校正者名',	'状態',	'状態の開始日', '底本名',	'出版社名',	'入力に使用した版',	'校正に使用した版']
df=pd.read_csv('GroupDouble_list_person_newnew_oldold_all_utf8.csv',names=names,header=0)

import re
import os
import glob
import shutil

#csvファイルの中身を1行ずつデータフレームに入れる。
#別のプログラムに
f3=open('newnew_oldold_list_pathlist_NAozora15.csv','w')
writer=csv.writer(f3)
names=["パス","作品名","著者名","仮名遣い種別"]
df2 = pd.read_csv('newnew_oldold_list_NAozora13.csv',names=names,header=None)
#print(df2["パス"])
#df2.columns=["パス","作品名","著者名","仮名遣い種別"]
#df_reset=df2.reset_index()
df3 =[]
for filepath, tytle, authorname, type in zip(df2["パス"], df2["作品名"],df2["著者名"],df2["仮名遣い種別"]):
    before = str(filepath)
    #print(before)
    #もしタイトル_著者名のフォルダが存在しなかったら新たに作成する。
    after='newnew_oldold_once_15/'+tytle+'_'+authorname
    if os.path.isdir(after)==False:
        os.mkdir(after)
    #一つの作品に対し、一つのテキストファイルが存在するテキストファイルをコピー
    #コピー元フォルダと、移動先のフォルダの両方が存在することを確認
    if os.path.isdir(before) and os.path.isdir(after) == True:
        print("true")
        #print(before)
        filename=os.listdir(before)
        for p in filename:
            shutil.copy(os.path.join(before, p), after)
            filename=os.listdir(before)
            data=[filepath]+[tytle]+[authorname]+[type]+filename
            writer.writerow(data)
    else:
        print("フォルダが見つかりません")
f3.close()
