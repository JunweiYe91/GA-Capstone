
# Import libraries
import pandas as pd
import numpy as np
import pandas as pd
import sklearn
import pickle
from PIL import Image
import altair as alt

# Modeling libraries
from sklearn.ensemble import RandomForestClassifier

# Streamlit
import streamlit as st
import streamlit.components.v1 as components
import altair as alt

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Set Page Title
st.set_page_config(page_title="Credit Card Analysis", layout="wide")

# Set the title
title = "Credit Card Analysis"
st.title(title)

# Set description
st.write("First of all, welcome! This is the place where you can check out the analysis performed on credit cards. Feel free to check it out!")
st.markdown("##")

# Define dropdown options
options = ["", "Select a card", "Cashback Cards Word Cloud", "Miles Cards Word Cloud", "Cashback Cards BiGram (Top 20)", "Cashback Cards TriGram (Top 20)",
            "Miles Cards BiGram (Top 20)", "Miles Cards TriGram (Top 20)", "Cards With the Highest NPS", "Cards With the Lowest NPS"]

# Import card pics
cashack_wordcloud = Image.open('image/word_cloud/cashback_wordcloud.png')
miles_wordcloud = Image.open('image/word_cloud/miles_wordcloud.png')

# Import BiGram and TriGram dataframe
cashback_bigram_df = pd.read_csv('dataset/cashback_bigram.csv')
cashback_trigram_df = pd.read_csv('dataset/cashback_trigram.csv')
miles_bigram_df = pd.read_csv('dataset/miles_bigram.csv')
miles_trigram_df = pd.read_csv('dataset/miles_trigram.csv')
highest_nps_df = pd.read_csv('dataset/highest_nps.csv')
lowest_nps_df = pd.read_csv('dataset/lowest_nps.csv')

# Define content
with st.container():
    col1, col2, col3, col4 = st.columns((1, 0.5, 0.5, 0.5))

    with col1:
        select_option = st.selectbox("Please select:", options)

        if select_option == "Cashback Cards Word Cloud":
            st.image(cashack_wordcloud)

        if select_option == "Miles Cards Word Cloud":
            st.image(miles_wordcloud)

        if select_option == "Cashback Cards BiGram (Top 20)":
            chart = (
                alt.Chart(cashback_bigram_df)
                .mark_bar()
                .encode(
                alt.X("Phrases", axis=alt.Axis(labelAngle=-45)),
                alt.Y("Count"),
                alt.Color("cashback_bigram_df:O", legend = None),
                alt.Tooltip(["Phrases", "Count"]),
                )
                .interactive()
            )

            st.altair_chart(chart, use_container_width=True)

        if select_option == "Cashback Cards TriGram (Top 20)":
            chart = (
                alt.Chart(cashback_trigram_df)
                .mark_bar()
                .encode(
                alt.X("Phrases", axis=alt.Axis(labelAngle=-45)),
                alt.Y("Count"),
                alt.Color("cashback_trigram_df:O", legend = None),
                alt.Tooltip(["Phrases", "Count"]),
                )
                .interactive()
            )

            st.altair_chart(chart, use_container_width=True)

        if select_option == "Miles Cards BiGram (Top 20)":
            chart = (
                alt.Chart(miles_bigram_df)
                .mark_bar()
                .encode(
                alt.X("Phrases", axis=alt.Axis(labelAngle=-45)),
                alt.Y("Count"),
                alt.Color("miles_bigram_df:O", legend = None),
                alt.Tooltip(["Phrases", "Count"]),
                )
                .interactive()
            )

            st.altair_chart(chart, use_container_width=True)

        if select_option == "Miles Cards TriGram (Top 20)":
            chart = (
                alt.Chart(miles_trigram_df)
                .mark_bar()
                .encode(
                alt.X("Phrases", axis=alt.Axis(labelAngle=-45)),
                alt.Y("Count"),
                alt.Color("miles_trigram_df:O", legend = None),
                alt.Tooltip(["Phrases", "Count"]),
                )
                .interactive()
            )

            st.altair_chart(chart, use_container_width=True)

        if select_option == "Cards With the Highest NPS":
            chart = (
                alt.Chart(highest_nps_df)
                .mark_bar()
                .encode(
                alt.X("Net Promoter Score"),
                alt.Y("Cards"),
                alt.Color("highest_nps_df:O", legend = None),
                alt.Tooltip(["Cards", "Net Promoter Score"]),
                )
                .interactive()
            )

            st.altair_chart(chart, use_container_width=True)

        if select_option == "Cards With the Lowest NPS":
            chart = (
                alt.Chart(lowest_nps_df)
                .mark_bar()
                .encode(
                alt.X("Net Promoter Score"),
                alt.Y("Cards"),
                alt.Color("lowest_nps_df:O", legend = None),
                alt.Tooltip(["Cards", "Net Promoter Score"]),
                )
                .interactive()
            )

            st.altair_chart(chart, use_container_width=True)

# sidebar contents
st.sidebar.image(Image.open('image/logo/logo.png'))
st.sidebar.write("For Careers/Business Opportunity, please contact me at:")
st.sidebar.write("**Email:** junwei.ye.sg@gmail.com")
st.sidebar.write("**Linkedin:** https://www.linkedin.com/in/ye-junwei/")
st.sidebar.write("**Github:** https://github.com/JunweiYe91/GA-Projects")
