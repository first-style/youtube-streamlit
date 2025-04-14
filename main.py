import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Streamlit Study')

st.write('プレぐれすばーの表示')
'Start ! ! ! '

lateest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    lateest_interation.text(f'Interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done ! ! !'


# df = pd.DataFrame({
#         '1列目': [1, 2, 3, 4],
#         '2列目': [10, 20, 30, 40],

# })


left_column, right_column = st.columns(2)
button = left_column.button('Display right column')
if button:
    right_column.write('Pushed Left Button')


expander  = st.expander('Question')
expander.write('Write Questtion this space')

# if st.checkbox('SHOW MAP'):
#     df = pd.DataFrame(
#         np.random.rand(200, 2)/[50, 50] + [35.69, 139.70],
#         columns=['lat', 'lon'] 
#     )
#     st.map(df)

# option = st.selectbox(
#     'What number do you like ?',
#     list(range(1, 11))
# )

# 'You like number is ', option, '!!'

# text = st.text_input(
#     'What your hobby ? '
# )

# 'My hobby is ', text , '!!'

# condition = st.slider(
#     'Whats up ?' , 0, 100, 50
# )

# 'Condition is ', condition



# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)


# st.dataframe(df, width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

"""
# 1
## 2
### 3

``` coment
import streamlit as st
import numpy as up
import pandas as pd
```

"""