import streamlit as st
import datetime
import pandas as pd

list = []

st.title('出退勤管理アプリ')



if st.button("出勤"):
    time = datetime.datetime.today()
    list.append([time])
    
df = pd.DataFrame(list,columns=['出勤時間']) #列名
with pd.ExcelWriter("出退勤管理.xlsx") as writer:
    df.to_excel(writer,index=False) #エクセルファイルに書き出し






