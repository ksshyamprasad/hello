import streamlit as st
import numpy as np
import pandas as pd
import time
st.title('My first app')
st.write("WRITE THE TEXT HERE")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
''''''
# My first app
Here's our first attempt at using data to create a table:
''''''
df = pd.DataFrame({
 'first column': [1, 2, 3, 4],
 'second column': [10, 20, 30, 40]
})
df
chart_data = pd.DataFrame(
 np.random.randn(20, 3),
 columns=['a', 'b', 'c'])
st.line_chart(chart_data)