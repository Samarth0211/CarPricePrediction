import streamlit as st
import pickle
import pandas as pd
from utils.prediction import predict_price


# model = pickle.load(open('App/models/RandomForestRegressor.pkl', 'rb'))
car = pd.read_csv('App/data/cleaned_car.csv')

st.title('Car Price Predictor')

brand = sorted(car['brand'].unique())
car_name = sorted(car['car_name'].unique())
year = sorted(car['year'].unique(), reverse=True)
fuel_type = car['fuel'].unique()
# seller_type = car['seller_type'].unique()
transmission = car['transmission'].unique()

def main():
    selected_company = st.selectbox('Select the company:', brand)
    filtered_car_names = car[car['brand'] == selected_company]['car_name'].unique()
    selected_car_model = st.selectbox('Select the model:', filtered_car_names)
    selected_year = st.selectbox('Select Year of Purchase:', year)
    selected_fuel_type = st.selectbox('Select the Fuel Type:', fuel_type)
    transmission_type = st.selectbox('Select Transmission:', transmission)
    kilometers_driven = st.text_input('Enter the Number of Kilometres that the car has traveled:')
    engine = st.text_input('Engine capacity: ')
    mileage = st.text_input('Mileage:')

    if st.button('Predict Price'):
        prediction_result = predict_price(selected_car_model, selected_company, selected_year, selected_fuel_type, transmission_type, kilometers_driven, mileage, engine)
        st.write(f'Prediction: ₹{prediction_result}')

    st.write('This app predicts the price of a car you want to sell. Fill in the details above.')

if __name__ == "__main__":
    main()

