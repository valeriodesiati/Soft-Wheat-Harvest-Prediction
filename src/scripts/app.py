import json
import joblib
import locale
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/returnValueForMap', methods=['POST'])
def returnValueForMap():
    dataForMap = pd.read_csv("../../data/processed/features.csv")
    Lat = dataForMap['lat']
    Lon = dataForMap['lon']
    Prod = dataForMap['produzione_media']

    stringReturn = ""
    for x in Lat:
        stringReturn = stringReturn + str(x) + ","
    stringReturn = stringReturn + "#"
    for x in Lon:
        stringReturn = stringReturn + str(x) + ","
    stringReturn = stringReturn + "#"
    for x in Prod:
        stringReturn = stringReturn + str(x) + ","

    return stringReturn

@app.route('/', methods=['GET'])
def form():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        alt = float(request.form['alt'])
        lat = float(request.form['lat'])
        lon = float(request.form['lon'])
        superficie = float(request.form['superficie_media'])
        prec = float(request.form['prec_media'])
        temp = float(request.form['temp_media'])
        
        model = joblib.load('../../models/rf_harvest_model.pkl')
        if model is None:
            return "Error: model not valid", 400

        input_data = pd.DataFrame({
            'alt': [alt],
            'lat': [lat],
            'lon': [lon],
            'superficie': [superficie],
            'prec': [prec],
            'temp': [temp],
        })
        
        print(input_data)

        prediction = np.array([tree.predict(input_data) for tree in model.estimators_])
        print(prediction)

        median_prediction = round(np.percentile(prediction, 50))
        lower_bound = round(np.percentile(prediction, 5))
        upper_bound = round(np.percentile(prediction, 95))

        locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')
        
        median_prediction = locale.format_string('%.0f', median_prediction, grouping=True)
        lower_bound = locale.format_string('%.0f', lower_bound, grouping=True)
        upper_bound = locale.format_string('%.0f', upper_bound, grouping=True)
        
        prediction_text = f'Average crop yield prediction: {median_prediction} quintals. <br> Range: {lower_bound} - {upper_bound} quintals.'
        print(f'Average crop yield prediction: {median_prediction} quintals. \nRange: {lower_bound} - {upper_bound} quintals.')
        
        return prediction_text
   
    except Exception as e:
        print(e)
        return f"Error during prevision: {str(e)}", 500
    
if __name__ == '__main__':
    app.run(debug=True)