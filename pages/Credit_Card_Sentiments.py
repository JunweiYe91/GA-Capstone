
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
st.set_page_config(page_title="Credit Card Sentiments", layout="wide")

# Set the title
title = "Credit Card Sentiments"
st.title(title)

# Set the logo
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

# Set description
st.write("First of all, welcome! This is the place where you can check out the sentiments and reviews of each card. Feel free to check it out!")
st.markdown("##")

# Define dropdown options
card_options = ["Select a card"]

# Import required datasets
nps_score = pd.read_csv("dataset/2. combined_nps_df.csv")
sentiments = pd.read_csv("dataset/2. combined_expand_df.csv")
card_list = pd.read_csv("dataset/card_list.csv")

for card in card_list['Full Name']:
    card_options.append(card)

# Import card pics
not_available = Image.open('image/cards/not_available.png')
hsbc_advance_card = Image.open('image/cards/hsbc_advance_card.png')
posb_everyday_card = Image.open('image/cards/posb_everyday_card.png')
sc_spree_card = Image.open('image/cards/sc_spree_card.png')
uob_one_card = Image.open('image/cards/uob_one_card.png')
citi_rewards_card = Image.open('image/cards/citi_rewards_card.png')
dbs_altitude_visa_card = Image.open('image/cards/dbs_altitude_visa_card.png')
dbs_womans_world_card = Image.open('image/cards/dbs_womans_world_card.png')
uob_prvi_miles_card = Image.open('image/cards/uob_prvi_miles_card.png')
standard_chartered_unlimited_cashback_credit_card = Image.open('image/cards/standard_chartered_unlimited_cashback_credit_card.png')
amex_true_cashback_card = Image.open('image/cards/amex_true_cashback_card.png')
ocbc_plus_visa_card = Image.open('image/cards/ocbc_plus_visa_card.png')
dbs_live_fresh = Image.open('image/cards/dbs_live_fresh.png')
cimb_platinum_mastercard_cashback = Image.open('image/cards/cimb_platinum_mastercard_cashback.png')
ocbc_365_credit_card = Image.open('image/cards/ocbc_365_credit_card.png')
citi_smrt_card = Image.open('image/cards/citi_smrt_card.png')
ocbc_cashflo_credit_card = Image.open('image/cards/ocbc_cashflo_credit_card.png')
cimb_visa_signature = Image.open('image/cards/cimb_visa_signature.png')
ocbc_plus_visa_card = Image.open('image/cards/ocbc_plus_visa_card.png')
ocbc_frank_credit_card = Image.open('image/cards/ocbc_frank_credit_card.png')
citi_cash_back_plus_card = Image.open('image/cards/citi_cash_back_plus_card.png')
citi_cash_back_card = Image.open('image/cards/citi_cash_back_card.png')
citi_premiermiles_visa_card = Image.open('image/cards/citi_premiermiles_visa_card.png')
amex_singapore_airlines_krisflyer_credit_card = Image.open('image/cards/amex_singapore_airlines_krisflyer_credit_card.png')
ocbc_titanium_rewards_card = Image.open('image/cards/ocbc_titanium_rewards_card.png')
hsbc_revolution_credit_card = Image.open('image/cards/hsbc_revolution_credit_card.png')
uob_preferred_platinum = Image.open('image/cards/uob_preferred_platinum.png')
ocbc_90_degrees_n_mastercard = Image.open('image/cards/ocbc_90_degrees_n_mastercard.png')

# Create a dictionary to store card images
card_details = {
    "Standard Chartered Unlimited Card": {
        "image": standard_chartered_unlimited_cashback_credit_card
    },
    "UOB One Card": {
        "image": uob_one_card
    },
    "POSB Everyday Card": {
        "image": posb_everyday_card
    },
    "Amex True Card": {
        "image": amex_true_cashback_card
    },
    "OCBC Ntuc Plus Visa Card": {
        "image": ocbc_plus_visa_card
    },
    "DBS Live Fresh Card": {
        "image": dbs_live_fresh
    },
    "CIMB Platinum Card": {
        "image": cimb_platinum_mastercard_cashback
    },
    "OCBC 365 Card": {
        "image": ocbc_365_credit_card
    },
    "Citi Smrt Card": {
        "image": citi_smrt_card
    },
    "Standard Chartered Spree Card": {
        "image": sc_spree_card
    },
    "OCBC Cashflo Card": {
        "image": ocbc_cashflo_credit_card
    },
    "CIMB Visa Signature": {
        "image": cimb_visa_signature
    },
    "HSBC Advance Card": {
        "image": hsbc_advance_card
    },
    "OCBC Plus Visa Card": {
        "image": ocbc_plus_visa_card
    },
    "OCBC Frank Card": {
        "image": ocbc_frank_credit_card
    },
    "Citi Cash Back Plus Card": {
        "image": citi_cash_back_plus_card
    },
    "Citi Cash Back Card": {
        "image": citi_cash_back_card
    },
    "DBS Altitude Visa Signature Card": {
        "image": dbs_altitude_visa_card
    },
    "DBS Womans World Card": {
        "image": dbs_womans_world_card
    },
    "Citi Rewards Card": {
        "image": citi_rewards_card
    },
    "UOB Preferred Platinum Visa Card": {
        "image": uob_preferred_platinum
    },
    "Citi Premiermiles Visa Card": {
        "image": citi_premiermiles_visa_card
    },
    "Amex Singapore Airlines Krisflyer Card": {
        "image": amex_singapore_airlines_krisflyer_credit_card
    },
    "UOB Prvi Miles Card": {
        "image": uob_prvi_miles_card
    },
    "OCBC 90 Degrees N Card": {
        "image": ocbc_90_degrees_n_mastercard
    },
    "OCBC Titanium Rewards Card": {
        "image": ocbc_titanium_rewards_card
    },
    "HSBC Revolution Card": {
        "image": hsbc_revolution_credit_card
    },
    "Select a card": {
        "image": not_available
    }
}

# Define content
with st.container():
    col1, col2, col3, col4 = st.columns((1.2, 0.5, 2, 0.5))
    #col1, col2, col3, col4 = st.columns((10, 0.5, 2, 0.5))
    with col1:
        st.subheader('Choose your card')
        selected_card = st.selectbox("Please select a card:", card_options)

        # Define outputs based on inputs
        selected_card_fullname = card_options[card_options.index(selected_card)]
        card_image = card_details[selected_card_fullname]['image']

        # Setting a condition if a choice isnt selected_card
        if selected_card_fullname == "Select a card":
            card_nps = 'Not available'
            card_reviews_no = 'Not available'
            card_sentiments = 'Not available'
        else:
            selected_card_name = card_list[card_list['Full Name'] == selected_card_fullname].reset_index()['Name'][0]
            card_nps = nps_score[nps_score['card_name'] == selected_card_name].reset_index(drop = True)['net_promoter_score'][0]
            card_reviews_no = nps_score[nps_score['card_name'] == selected_card_name].reset_index(drop = True)['no_of_reviews'][0]
            card_sentiments = sentiments[sentiments['credit_card_name']==selected_card_name].reset_index(drop = True).iloc[:, 2:]

        # Display outputs
        st.image(card_image)
        st.write("")
        st.write("**Net Promoter Score:** " + str(card_nps) + " /100")
        st.write("**Number of reviews:** " + str(card_reviews_no))


with st.container():
    st.write("**Reviews:**")

    # Checkboxs
    filter_sentiment = st.radio(label = 'Filter Sentiment Rating:', options = ['All','1','2', '3', '4', '5'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # Filters the dataframe based on inputs from the checkbox
    if filter_sentiment == 'All':
        st.write(card_sentiments)
    else:
        st.write(card_sentiments[card_sentiments['sentiment'] == int(filter_sentiment)])
