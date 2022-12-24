import streamlit as st;
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title("Hello")
st.header("Hell")
st.subheader("subhell")
st.markdown(''' # hh''')
st.write(st)
st.write({'fvieubv': 123})

data=pd.DataFrame(np.random.randn(100,3), columns=['a','b', 'c'])
st.line_chart(data)
st.bar_chart(data)

plt.scatter(data['a'],data['b'])
# st.pyplot()
st.graphviz_chart(""" digraph{like->share
 share ->more more -> like} """)