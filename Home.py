
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
st.set_page_config(page_title="Home Page", layout="wide")

# Set the title
title = "Welcome to KEYCARDS!"
st.title(title)

# sidebar contents
st.sidebar.image(Image.open('image/logo/logo.png'))
st.sidebar.write("For Careers/Business Opportunity, please contact me at:")
st.sidebar.write("**Email:** ye_junwei@hotmail.com")
st.sidebar.write("**Github:** https://github.com/JunweiYe91/GA-Projects")

# Set the content
with st.container():
    st.write("Welcome to KEYCARD, your one stop shop for credit related services. Feel free to explore！")
