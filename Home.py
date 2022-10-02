
# Import libraries
import pandas as pd
import numpy as np
import pandas as pd
import sklearn
import pickle
from PIL import Image

# Modeling libraries
from sklearn.ensemble import RandomForestClassifier

# Streamlit
import streamlit as st
import streamlit.components.v1 as components

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Set Page Title
st.set_page_config(page_title="Home", layout="wide")

# Set the title
title = "Welcome to KEYCARDS!"
st.title(title)

# sidebar contents
st.sidebar.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://lh3.googleusercontent.com/eRZ62FDqGZphgSBxSlibMF-6aNpRCIVslttJJLlsVbyECA6wVcT-KEtZOQ-FfY0VVzIFznTvTXK3eHYd7gjtfXQ1OZnd1z1pM81BiDjit_I7tqp93f7qzASs6I8tmMKkgtVhqjgktrk=w2400);
                background-repeat: no-repeat;
                padding-top: 2px;
                background-position: 20px 30px;
            }
        </style>
        """,
        unsafe_allow_html=True,
)

st.sidebar.write("For Careers/Business Opportunity, please contact me at:")
st.sidebar.write("**Email:** ye_junwei@hotmail.com")
st.sidebar.write("**Github:** https://github.com/JunweiYe91/GA-Projects")

# Set the content
with st.container():
    st.write("Welcome to KEYCARD, your one stop shop for credit related services. Feel free to explore！")
