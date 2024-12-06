# Soft Wheat Yield Prediction in Italy

## Overview

The aim of this project is to create a regression model to predict soft wheat yields based on geographic data (altitude, latitude, and longitude) of the land, historical series (from 2006 to 2021) of cultivated areas, annual yields, and measurements of temperature and precipitation.

## Installation

1. Clone the repository: `git clone https://github.com/valeriodesiati/Soft-Wheat-Harvest-Prediction`.
2. Install the dependencies and run the Flask app: `./start`.
3. Visit the link `https://127.0.0.1:5000` in your browser.

## Project Structure

- `/data`: Contains raw and processed data.
  - `/processed`: Processed data.
    - `dataset_final.csv`: Final unaggregated data.
    - `features.csv`: Aggregated final data.
  - `/raw`: Raw data.
- `/models`: Contains trained model save files.
- `/src`: Source code of the project.
  - `/scripts`: Scripts.
    - `/templates`: Flask web app interface.
    - `app.py`: Flask app.
  - `/notebooks`: Jupyter notebooks.
    - `1-prep_coltivazioni.ipynb`: Data preprocessing for wheat yields.
    - `2-prep_temp_prec.ipynb`: Data preprocessing for temperature and precipitation.
    - `3-prep_geo.ipynb`: Data preprocessing for geographic data.
    - `4-final.ipynb`: Final data merge.
    - `5-train_model.ipynb`: Model training with aggregated data.
    - `5b-train_model_all_data.ipynb`: Model training with unaggregated data.
    - `5c-esp_data_predictions.ipynb`: Prediction made using our model using spanish harvesting, temperature and precipitation data.
    - `5d-india_data_predictions.ipynb`: Prediction made using our model using indian harvesting, temperature and precipitation data.
    - `6-italy_future_weather.ipynb`: According to some research papers, in 2050 Italy's climate condition will very with a +2.5 °C and -1.5% precipitation. We adjusted our data with this indication and made predictions with our model.

## License

Creative Commons Zero v1.0 Universal.

## Contacts

Valerio Desiati - <valerio.desiati@studio.unibo.it> \
Lucrezia Ilvento - <lucrezia.ilvento@studio.unibo.it> \
Alberto Casado Moreno - <alberto.casadomoreno@studio.unibo.it>
