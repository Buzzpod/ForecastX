# ForecastX
Linear and nonlinear time series analysis for stock forecasting

# Linear Time Series Analysis
Placeholder text ..............................
## ARMA + GARCH
Placeholder text ..............................

# Nonlinear Time Series Analysis
Placeholder text ..............................
## Long-Short-Term Memory Model (LSTM)
Placeholder text ..............................
### Input Data Structure
![diagram](https://github.com/Buzzpod/ForecastX/blob/main/Diagrams/lstm_data_structure.PNG?raw=true)

### Notable models
Optimising LSTM models is an incremental process but every model that is trained in this project is saved in the "Models" folder. Below is a list of some notable models and some more indormation about them:

* **24-07-2023_14-42-13:** This is a multivariate LSTM model that predicts the daily close price of NVIDIA stock. It was trained on 5 variables (Close, Open, High, Low, Volume). The Bayesian optimisation in this case determined that the optimal parameters were (hidden_size=128, num_stacked_layers=2, learning_rate=0.005439, dropout=0.00) and it achieved repectable performance with Win-rate=54.84%, RMSE=18.31, MAE=12.67, MAPE=3.49 and R2=0.91
