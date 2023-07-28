# ForecastX
Linear and nonlinear time series analysis for stock forecasting

# Linear Time Series Analysis
The linear methods explored in this repository include:
* Autoregressive (AR) univariate model
* Moving average (MA) univariate model
* Autoregressive moving average (ARMA) univariate and multivariate model
* Seasonal autoregressive moving average (ARMA) univariate and multivariate model
* Generalsied autoregressive conditional heteroscedastic (GARCH) model

The respective notebooks are detailed as follows:

### AR Model
See notebook "NVDA_AR_MA.ipynb"

### MA Model
See notebook "NVDA_AR_MA.ipynb"

### ARMA + GARCH Univariate and Multivariate Model
See notebook "NVDA_ARMA_GARCH.ipynb"

### SARIMA + GARCH Univariate and Multivariate Model
See notebook "NVDA_SARIMA_GARCH.ipynb"

# Nonlinear Time Series Analysis
The main nonlinear method explored in this repositiory is long-short-term memory networks (LSTM) in several flavours as we attempt to find the optimal LSTM model for predicting the daily NVIDIA stock price. We start with a simple univariate LSTM (see "NVDA_UNIVARIATE_LSTM.ipynb") and move on to more complex models later on (see "NVDA_MULTIVARIATE_LSTM_SMALL.ipynb", "NVDA_MULTIVARIATE_LSTM_MEDIUM.ipynb"). We will also perform feature analysis when working on the more complex LSTM models in seperate notebooks too.

Finally, we will explore ensemble methods by using model-averaging techniques to achieve even greater performance by compbining several of the previously constructed models.

### Long-Short-Term Memory Model (LSTM)
#### Input Data Structure
![diagram](https://github.com/Buzzpod/ForecastX/blob/main/Diagrams/lstm_data_structure.PNG?raw=true)

#### Notable models
Optimising LSTM models is an incremental process but every model that is trained in this project is saved in the "Models" folder. Below is a list of some notable models and some more indormation about them:

* **24-07-2023_14-42-13:** This is a multivariate LSTM model that predicts the daily close price of NVIDIA stock. It was trained on 5 variables (Close, Open, High, Low, Volume). The Bayesian optimisation in this case determined that the optimal parameters were (hidden_size=128, num_stacked_layers=2, learning_rate=0.005439, dropout=0.00) and it achieved repectable performance with Win-rate=54.84%, RMSE=18.31, MAE=12.67, MAPE=3.49 and R2=0.91
