# prediction.py
import numpy as np
import pandas as pd
import pickle

def predict_price(selected_car_model, selected_company, selected_year, selected_fuel_type, transmission, kilometers_driven, mileage, engine):
    model = pickle.load(open('App/models/RandomForestRegressor.pkl', 'rb'))

    input_data = np.array([selected_car_model, selected_company, selected_year, selected_fuel_type, transmission, kilometers_driven, mileage, engine]).reshape(1, 8)
    prediction = model.predict(pd.DataFrame(columns=['car_name', 'brand', 'year', 'fuel', 'transmission', 'km_driven', 'mileage', 'engine'], data=input_data))
    return round(prediction[0], 2)
