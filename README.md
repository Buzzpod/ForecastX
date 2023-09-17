# ForecastX
Linear and nonlinear time series analysis methods for forecasting daily adjusted close prices of NVIDIA stock.

Note: this repository contains the coded elements of the dissertation titled "Enhancing Stock Forecasting using Linear and Nonlinear Time Series Analysis" by George Spyrou as part of the MSc Mathematical Finance degree at the University of Warwick / Warwick Business School. This dissertation was supervised by Dr Randa Herzallah.

# Linear Time Series Analysis
The linear methods explored in this repository include:
* Autoregressive (AR) univariate model
* Moving average (MA) univariate model
* Autoregressive integrated moving average (ARIMA) univariate and multivariate model
* Seasonal autoregressive integrated moving average (ARIMA) univariate and multivariate model
* Generalsied autoregressive conditional heteroscedastic (GARCH) model

The respective notebooks are detailed as follows:

See notebook "NVDA_ARMA_GARCH.ipynb" where we fit an optimise both univariate and multivariate linear models. The 'best' model achieved in this notebook is a multivariate ARMA + GARCH model, however, by starting with a SARIMA model, we effectively tested AR, MA, ARMA, ARIMA and SARIMA but found, through the optimisation process, that ARMA + GARCH achieved the best performance.



# Nonlinear Time Series Analysis
The main nonlinear method explored in this repositiory is long-short-term memory networks (LSTM) in several flavours as we attempt to find the optimal LSTM model for predicting the daily NVIDIA stock price. We start with a simple univariate LSTM (see "NVDA_LSTM_SMALL.ipynb") and move on to more complex architectures later on (see "NVDA_LSTM_MEDIUM.ipynb", "NVDA_LSTM_LARGE.ipynb", "NVDA_LSTM_FINAL.ipynb"). We will also perform feature analysis when working on the more complex LSTM models in seperate notebooks too.

Finally, we will explore ensemble methods by using model-averaging techniques to achieve even greater performance by compbining several of the previously constructed models. This can be found in the file "NVDA_ENSEMBLE.ipynb".

# Saved Models
Throughout the process of optimising and experimenting with different model architectures, we will end up training dozens of models in total. All models trained along the way are saved so they can be loaded back in at later dates to perform further testing. All models are saved in the "Models" sub-directory.

# Dependencies and Executing Notebooks
In the linear section, we make heavy use of core Python libraries such as Scikit-Learn, Pandas, Statsmodels and the Arch library.

In the nonlinear section, we use PyTorch for implementing the LSTM networks and the notebooks have also been configured to use GPU optimisation whic requires the user to have a supported Nvidia GPU installed in their system along with the necessary software and drivers such as CuDNN.

As a result, it is advised that users who do not have access to the necessary system configurations do not attempt to run the nonlinear notebooks, but instead read through the executed notebooks where the outputs are visible without having to run them.

# Contact
For any queries on the contents of this repository or this dissertation in general, please contact George Spyrou via email (george.spyrou@warwick.ac.uk)