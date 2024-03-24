import streamlit as st
import time
st.title('Streamlit')
st.write('Progresbar')
'Start!!'
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)


left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
expander=st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text=st.sidebar.text_input('貴方の趣味を教えてください')
condision=st.sidebar.slider('あなたの今の調子は？',0,100,50)
'貴方の趣味は',text,'です'
'貴方の状態：',condision

