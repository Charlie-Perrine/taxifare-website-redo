import streamlit as st
import datetime
import requests

# 1. Title
st.markdown("<h1 style='text-align: center; color: purple;'>Batch 1117 ❀*ੈ✩‧₊˚ Taxifare</h1>", unsafe_allow_html=True)

# 2. Description of the website
st.markdown('''

 Returns a prediction of the price of a fare in New York City based on certain parameters.

''')
st.markdown("<h6 style='text-align: center;'> ⋆｡ ﾟ☁︎｡ ⋆｡ ﾟ☾ ﾟ｡ ⋆</h6>", unsafe_allow_html=True)


# Adds snow, it's cute •⩊•
#st.snow()

# 3. Changes the font of the markdown to Roboto.
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Caveat');

			html, body, [class*="css"]  {
			font-family: 'Caveat', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

# 4. Get the parameters for the prediction
'''
### Please fill out the following form:
'''

pickup_date = st.date_input('Pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('Pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}'
pickup_longitude = st.number_input('Pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('Pickup latitude', value=-73.9798156)
dropoff_longitude = st.number_input('Dropoff longitude', value=40.6413111)
dropoff_latitude = st.number_input('Dropoff latitude', value=-73.7803331)
passenger_count = st.number_input('Passenger_count', min_value=1, max_value=8, step=1, value=1)


# 5. Put all of the parameters in a dictionary

params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)


# 6. API Url
api_url = 'https://taxifare.lewagon.ai/predict'


# 7. Call the API using the requests package
response = requests.get(api_url, params=params)

print(response.json())

prediction = response.json()['fare']

# 8. Print the prediction out

st.header(f'Fare amount: ${round(prediction, 2)}')





# WAGON SOLUTION

# import streamlit as st

# import datetime
# import requests

# '''
# # TaxiFareModel front

# This front queries the Le Wagon [taxi fare model API](https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2)
# '''

# with st.form(key='params_for_api'):

#     pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
#     pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
#     pickup_datetime = f'{pickup_date} {pickup_time}'
#     pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
#     pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
#     dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
#     dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
#     passenger_count = st.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

#     st.form_submit_button('Make prediction')

# params = dict(
#     pickup_datetime=pickup_datetime,
#     pickup_longitude=pickup_longitude,
#     pickup_latitude=pickup_latitude,
#     dropoff_longitude=dropoff_longitude,
#     dropoff_latitude=dropoff_latitude,
#     passenger_count=passenger_count)

# wagon_cab_api_url = 'https://taxifare.lewagon.ai/predict'
# response = requests.get(wagon_cab_api_url, params=params)

# prediction = response.json()

# pred = prediction['fare']

# st.header(f'Fare amount: ${round(pred, 2)}')
