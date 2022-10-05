
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

# Set the logo
st.sidebar.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://keycards.herokuapp.com/media/2a12f60e3ce1cf799cc4dbf2266d4ea295ad072fa304131800d2a345.png);
                background-repeat: no-repeat;
                background-size: 250px 49px;
                padding-top: 2px;
                background-position: 20px 30px;
            }
        </style>
        """,
        unsafe_allow_html=True,
)

# sidebar contents
#st.sidebar.image(Image.open('image/logo/logo.png'))
#st.sidebar.write("For Careers/Business Opportunity, please contact me at:")
#st.sidebar.write("**Email:** junwei.ye.sg@gmail.com")
#st.sidebar.write("**Linkedin:** https://www.linkedin.com/in/ye-junwei/")
#st.sidebar.write("**Github:** https://github.com/JunweiYe91/GA-Projects")

# Set the content
with st.container():
    st.write("Welcome to KEYCARD, your one stop shop for credit related services. Feel free to explore！")
    st.write("For mobile users, please click on the \">\" button on the top right corner of the page.")
    st.write("")
    st.write("")

    st.image(Image.open('image/logo/Logo(Small).png'))
    st.write("**For Careers/Business Opportunity, please contact me at:**")
    st.write("**Email:** junwei.ye.sg@gmail.com")
    st.write("**Linkedin:** https://www.linkedin.com/in/ye-junwei/")
    st.write("**Github:** https://github.com/JunweiYe91/GA-Projects")
