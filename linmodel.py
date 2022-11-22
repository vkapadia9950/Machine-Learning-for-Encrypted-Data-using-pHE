import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import PolynomialFeatures
from tqdm import tqdm

class LinModel:
	def __init__(self):
		pass

	def polygetResults(self):
		df=pd.read_csv("HospitalCosts.csv")
		df = df.dropna()
		y=df.TOTCHG
		X=df.drop('TOTCHG',axis=1)
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=37)
		degree=2
		poly_model = PolynomialFeatures(degree=degree)

		# transform out polynomial features
		poly_x_values = poly_model.fit_transform(X_train.values)
		poly_model.fit(poly_x_values, y_train.values)
		regression_model = LinearRegression()
		regression_model.fit(poly_x_values, y_train.values)
		y_pred = regression_model.predict(poly_model.fit_transform(X_test.values))

		RMSE=pow(mean_squared_error(y_pred, y_test),0.5)
		R=r2_score(y_pred, y_test)
		print(regression_model.score(poly_model.fit_transform(X_train.values),y_train))
		print(regression_model.score(poly_model.fit_transform(X_test.values),y_test))
		return regression_model, poly_model, y_pred, RMSE, R

	def getResults(self):
		df=pd.read_csv('HospitalCosts.csv')
		df = df.dropna()
		y=df.TOTCHG
		X=df.drop('TOTCHG',axis=1)
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=23)
		regression_model = LinearRegression().fit(X_train, y_train)
		y_pred=regression_model.predict(X_test)
		RMSE=pow(mean_squared_error(y_pred, y_test),0.5)
		R=r2_score(y_pred, y_test)
		# print(regression_model.score(X_train,y_train))
		# print(regression_model.score(X_test,y_test))
		return regression_model, y_pred, RMSE, R

	def getWeights(self):
		# reg, poly_model, y_pred, RMSE, R = self.polygetResults()
		# coef, inter, power = reg.coef_, reg.intercept_, poly_model.powers_
		reg = self.getResults()[0]
		return reg.coef_, reg.intercept_

		
def train():
    	coef, inter= LinModel().getWeights()
	

if __name__=='__main__':
	for i in tqdm(range(1), desc="Training Model"):
		train()
	print("---------------------------------")
	print("THE MODEL IS READY FOR PREDICTION")
	print("---------------------------------")
	

