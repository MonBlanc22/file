import pandas as pd
import csv
#印刷・表示する行数、列数の上限を設定しない。
pd.options.display.max_rows=None
pd.options.display.width=None
names=['人物ID',	'著者名',	'作品ID',	'作品名',	'仮名遣い種別',	'翻訳者名等',	'入力者名',	'校正者名',	'状態',	'状態の開始日', '底本名',	'出版社名',	'入力に使用した版',	'校正に使用した版']
df=pd.read_csv('Double_list_person_all_utf8.csv',names=names,header=0)
#重複するファイルの数を数える。
#keep=Falseとすることで、重複ファイルの一番目もTrueになる。
#作品一覧から仮名遣い種別が新字新仮名のものを削除する。
drop_row1=df.index[df['仮名遣い種別'] == '新字旧仮名']
drop_row2=df.index[df['仮名遣い種別'] == '旧字新仮名']
dropped_df1=df.drop(drop_row1)
dropped_df2=dropped_df1.drop(drop_row2)
#著者名、作品名が重複し、かつ仮名遣い種別が重複するものを削除
#ただし、重複するものの１番目は削除しない
drop_row3=dropped_df2.index[dropped_df2.duplicated(subset=['著者名','作品名','仮名遣い種別'])]
dropped_df3=dropped_df2.drop(drop_row3)
#'著者名','作品名'が重複するものを残す
#新字旧仮名を含まない重複ファイルの一覧をcsv形式で出力
new_dataframe=dropped_df3[dropped_df3.duplicated(subset=['著者名','作品名'],keep=False)]
writefile='GroupDouble_list_person_newnew_oldold_all_utf8.csv'
#csvファイルに書き出す
new_dataframe.to_csv('GroupDouble_list_person_newnew_oldold_all_utf8.csv')
#Non_Doubleデータフレームの行数を取得
print(len(new_dataframe))
