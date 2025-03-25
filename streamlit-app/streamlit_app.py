import streamlit as st
import pandas as pd
import numpy as np

st.title("My Streamlit App 🚀")

st.write("This is a simple web app using Streamlit.")

# Create a simple chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)
