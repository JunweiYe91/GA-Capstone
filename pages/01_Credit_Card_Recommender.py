
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
st.set_page_config(page_title="Credit Card Recommendation", layout="wide")

# Set the title
title = "Credit Card Recommendation Engine"
st.title(title)

# Allow cache
#@st.cache(allow_output_mutation=True)

# Set description
st.write("First of all, welcome! This is the place where you can input your spendings and our system \
        will recommend a credit card that best suits you. Try it now and optimise your savings every month!")
st.markdown("##")

# Define sidebar title
st.sidebar.header('Input your monthly expenses')

# Define dropdown options
ques_1_options = ['','Cashback', 'Miles']
ques_2_options = ['','Yes', 'No']
ques_3_options = ['', 'Less than 30,000', '30,000 - 39,999', '40,000 - 49,000', '50,000 - 59,000', '60,000 to 69,999',
                    '70,000 to 79,999', '80,000 or more']
ques_4_options = ['', 'Public Transport', 'Esso', 'Shell', 'SPC', 'Caltex']
ques_5_options = ['', '0', '1 - 199', '200 - 399', '400 - 499', '600 - 799', '800 - 999', 'More than 1000']
ques_6_options = ['', '0', '1 - 199', '200 - 399', '400 - 499', '600 - 799', '800 - 999', 'More than 1000']
ques_7_options = ['', 'Ntuc', 'Giant', 'Cold Storage', 'Sheng Shiong', 'Redmart']
ques_8_options = ['', '0', '1 - 199', '200 - 399', '400 - 499', '600 - 799', '800 - 999', 'More than 1000']
ques_9_options = ['', '0', '1 - 199', '200 - 399', '400 - 499', '600 - 799', '800 - 999', 'More than 1000']
ques_10_options = ['', '0', '1 - 199', '200 - 399', '400 - 499', '600 - 799', '800 - 999', 'More than 1000']
ques_11_options_v1 = ['', 'Not available for cashback cards']
ques_11_options_v2 = ['', 'Not available for cashback cards', 'Krisflyer', 'Asia Miles', 'Frequent Flyer', 'Big Loyalty',
                    'British Airways Executive Club', 'Etihad Guest', 'Turkish Miles and Smiles']

# Set the input parameters
with st.sidebar.form(key = 'Form_1'):
    ques_1 = st.selectbox(
        'Do you prefer a miles or cashback card?',
        ques_1_options
    )
    ques_2 = st.selectbox(
        'Are you a Singaporean?',
        ques_2_options
    )
    ques_3 = st.selectbox(
        'What is your annual income?',
        ques_3_options
    )
    ques_4 = st.selectbox(
        'Where do you normally go to for petrol refuel?',
        ques_4_options
    )
    ques_5 = st.selectbox(
        'How much do you spend on petrol/public transport every month? This should be the net price \
        after all available discounts.',
        ques_5_options
    )
    ques_6 = st.selectbox(
        'How much do you spend on dining every month?',
        ques_6_options
    )
    ques_7 = st.selectbox(
        'Where do you usually shop for groceries?',
        ques_7_options
    )
    ques_8 = st.selectbox(
        'How much do you spend on groceries every month?',
        ques_8_options
    )
    ques_9 = st.selectbox(
        'How much do you spend on Grab every month?',
        ques_9_options
    )
    ques_10 = st.selectbox(
        'How much do you spend online shopping every month?',
        ques_10_options
    )
    if ques_1 == 'Cashback':
        ques_11 = st.selectbox(
            'Which is your preferred travel partner?',
            ques_11_options_v1)
    else:
        ques_11 = st.selectbox(
            'Which is your preferred travel partner?',
            ques_11_options_v2)
    st.write("")

    st.form_submit_button("Submit")

# Saving the input as a dataframe
def user_input():
    data = {'ques_1': ques_1_options.index(ques_1),
        'ques_2': ques_2_options.index(ques_2),
        'ques_3': ques_3_options.index(ques_3),
        'ques_4': ques_4_options.index(ques_4),
        'ques_5': ques_5_options.index(ques_5),
        'ques_6': ques_6_options.index(ques_6),
        'ques_7': ques_7_options.index(ques_7),
        'ques_8': ques_8_options.index(ques_8),
        'ques_9': ques_9_options.index(ques_9),
        'ques_10': ques_10_options.index(ques_10),
        'ques_11': ques_11_options_v2.index(ques_11)}
    inputs = pd.DataFrame(data,index=[0])
    return inputs

df = user_input()

# Act as a check to check the inputs
#@st.subheader('User Input Parameters')
#st.write(df)

# Import the model_selection
pickled_model = pickle.load(open('model.pkl', 'rb'))

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

# Define card details
card_details = {
    '1': {
        'name': 'Not eligble for any card',
        'image': not_available,
        'free_gift': "No signup gifts."
        },
    '2': {
        'name': 'HSBC Advance Card',
        'image': hsbc_advance_card,
        'free_gift': "Get Samsonite Prestige 69cm Spinner Exp worth \$670 / \$200 with \$500 min spend."
        },
    '3': {
        'name': 'POSB Everyday Cashback Card',
        'image': posb_everyday_card,
        'free_gift': "Get S\$150 cashback when you apply with the promo code 150CASH and make a min spend of S\$800 within 60 days of card approval."
        },
    '4': {
        'name': 'Standard Chartered Spree Card',
        'image': sc_spree_card,
        'free_gift': "Get up to S\$220 cashback when you spend S\$200."
        },
    '5': {
        'name': 'UOB One Card',
        'image': uob_one_card,
        'free_gift': "No signup gifts."
        },
    '6': {
        'name': 'Citi Rewards Card',
        'image': citi_rewards_card,
        'free_gift': "Sign up on SingSaver to receive a Apple iPad 9th Gen (worth S\$499) or an ErgoTune Supreme V3 (worth S\$850) or the latest Apple Watch SE 2nd Gen (worth S\$379) or S\$350 cash"
        },
    '7': {
        'name': 'DBS Altitude Visa Card',
        'image': dbs_altitude_visa_card,
        'free_gift': "Get S\$150 cashback. Enter the promo code 150CASH and make a min spend of S\$800 within 60 days of card approval to be eligible."
        },
    '8': {
        'name': 'DBS Womans World Card',
        'image': dbs_womans_world_card,
        'free_gift': "Get S\$150 cashback. Enter the promo code 150CASH and make a min spend of S\$800 within 60 days of card approval to be eligible."
        },
    '9': {
        'name': 'UOB Prvi Miles Card',
        'image': uob_prvi_miles_card,
        'free_gift': "No signup gifts."
        }
    }


# Make the prediction
prediction = pickled_model.predict(df)
prediction_name = card_details[str(prediction[0])]['name']
prediction_pic = card_details[str(prediction[0])]['image']
prediction_free_gift = card_details[str(prediction[0])]['free_gift']

# Returns the details of the predictions
st.subheader('Prediction')
st.image(prediction_pic)
st.write('**Card Name:**' + ' ' + prediction_name)
st.write('**First Time Users:**' + ' ' + prediction_free_gift)
st.write("")

# List of cards in the recommender
st.markdown(
"""
**List of cards included in the recommender:**
- Citi Rewards Miles Card
- DBS Altitude Visa Card
- DBS Womans World Miles Card
- HSBC Advance Card
- POSB Everyday Cashback Card
- Standard Chartered Spree Card
- UOB One Card
- UOB Prvi Miles Card
"""
)
