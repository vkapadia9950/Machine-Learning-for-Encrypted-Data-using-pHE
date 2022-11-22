# Machine-Learning-for-Encrypted-Data-using-pHE

## 1. Python Packages Installation
* Run the following commands in terminal to install dependent python libraries used in code

		`pip3 install -r requirements.txt`

## 2. Training Model
After the initial installation is successfully done. The linear regression model training can be done by the following command:

	`python3 linmodel.py`
  
## 3. Predicting Hospital Cost using Homomorphically Encrypted Data
After the training of model is successfully done. The model is ready to be used for prediction:

	`python3 customer.py`
  
### 3.1 Send Encrypted Data
  
 Select `S` to send encrypted data to server.
 
 ### 3.2 Compute Predictions
  
 Select `P` to start computation of result on server.
 
 
 ### 3.3 Decrypt and Load Result
  
 Select `L` to decrypt an encrypted result received from server and load it.
 
