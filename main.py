#import
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.01)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたが趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 50, 100)

# 'あなたの好きな趣味:', text
# 'コンディション:', condition

# if st.checkbox('Show Image'):
#     img = Image.open('sigur_ros1.jpg')
#     st.image(img, caption='Sigur Ros New Album', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['latitude', 'longitude']
# )

#map
# st.map(df)

#st.table(df.style.highlight_max(axis=0))