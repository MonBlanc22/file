import pandas as pd
import csv
#印刷・表示する行数、列数の上限を設定しない。
pd.options.display.max_rows=None
pd.options.display.width=None
names=['人物ID',	'著者名',	'作品ID',	'作品名',	'仮名遣い種別',	'翻訳者名等',	'入力者名',	'校正者名',	'状態',	'状態の開始日',	'底本名',	'出版社名',	'入力に使用した版',	'校正に使用した版']
df=pd.read_csv('list_person_all_utf8.csv',names=names,header=0)
#print(df.head())
#重複するファイルの数を数える。
#keep=Falseとすることで、重複ファイルの一番目もTrueになる。
print(df.duplicated(subset=['著者名','作品名'],keep=False).sum())
#print(df.duplicated(subset=['著者名','作品名'],keep=False))
#print(pd.options.display.max_rows)#デフォルトは60
#print(df[df.duplicated(subset=['著者名','作品名'],keep=False)])
#
writefile='Double_list_person_all_utf8.csv'
dataframe=df[df.duplicated(subset=['著者名','作品名'],keep=False)]
#csvファイルに書き出す
dataframe.to_csv('Double_list_person_all_utf8.csv')
