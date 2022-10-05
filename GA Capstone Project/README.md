# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone Project : Credit Card Recommender

### Project Objectives:

You've want to sign up for a credit card that best fits you, but you've realised that you will need to comb through all card descriptions, conditions and reviews in order to decide which card is the best. You find that it is very inconvenient and as a data scientist, you decide to take it upon yourself to build a credit card recommender.

Use different techniques to analyse the reviews, credit card conditions to derive a credit card recommender that could help to save a lot of time when choosing a credit card.

---

### Data used:

Data in this used in the analysis consists of credit card details and reviews scrapped from various websites. Please rerefer to the data dictionary for more information on the columns extracted.

---

### Background

All credit cards in Singapore offer some sort of reward for using them for your purchases, which include incentives like cashback, reward points (which can be traded for air miles, discount vouchers or actual products), or airline miles. However, the most common reward, and perhaps the most enticing, would perhaps be cashback.

For the uninitiated, cashback refers to receiving back a percentage of what you spend in the form of money. It is akin to getting a perpetual discount whenever you spend. Sounds too good to be true? It really is not. Credit card companies are constantly competing to provide the most competitive rewards for their customers - some cards offer lucrative sign-up promotions, while others offer higher cashbacks for niche spending categories like travel or sustainability.

With so many cards available on the market to choose from, it is no wonder that Singaporeans have a hard time deciding which is the best credit card in Singapore. In particular, it is hard to compare the different cashback rewards across multiple categories for various credit cards. [(source)](https://sg.news.yahoo.com/three-reasons-why-own-credit-104237659.html)

---

### Data Dictionary:

<br>**Dataset name: `cashback_expand_df`**
<br>This dataset contains all the reviews on cashback credit cards.

| Feature | Type | Dataset | Description |
|:--|:-:|:-:|:--|
|credit_card_name|string|perfumes_df|Name of the credit card.|
|card_type|string|perfumes_df|Type of credit card. Cashback of Air Miles.|
|reviews|string|perfumes_df|Reviews on the credit cards.|


<br>**Dataset name: `miles_expand_df`**
<br>This dataset contains all the reviews on air miles credit cards.

| Feature | Type | Dataset | Description |
|:--|:-:|:-:|:--|
|credit_card_name|string|perfumes_df|Name of the credit card.|
|card_type|string|perfumes_df|Type of credit card. Cashback of Air Miles.|
|reviews|string|perfumes_df|Reviews on the credit cards.|

<br>**Dataset name: `combined_expand_df`**
<br>This dataset contains all the reviews on all credit cards.

| Feature | Type | Dataset | Description |
|:--|:-:|:-:|:--|
|credit_card_name|string|perfumes_df|Name of the credit card.|
|card_type|string|perfumes_df|Type of credit card. Cashback of Air Miles.|
|reviews|string|perfumes_df|Reviews on the credit cards.|

---

### Key takeaways from the project:
1. Recommender deployed successfully on https://keycards.herokuapp.com/
2. The recommender is fuss free way to select the best suited credit cards. The recommender uses a Random Forest Model with a model accuracy of 94%.
3. Besides card return, customers service is also quite an important factor when determining a good credit card.

---

### Limitations and Future Enhancements
1. Analysis is only limited to all the reviews that have been successfully scrapped. Suggest extracting reviews from other sites as well.
2. Recommender only has 8 cards at the moment. To include more credit cards in the future.
3. Recommender could be scaled to include credit cards for other countries.
---ß

