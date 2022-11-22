from linmodel import LinModel
import phe as paillier
import json
import numpy as np
from tqdm import tqdm


def getData():
	for i in tqdm(range(1), desc="Retriving Data File"):
		with open('enc_data.json', 'r') as file: 
			d=json.load(file)
		data=json.loads(d)
	return data

# def generate_poly_prediction(data, powers, coef, intercept):
# 	data = np.array(data)
# 	result = []
# 	for i in range(len(powers)):
# 		temp = 1
# 		for j in range(len(powers[0])):
# 			temp *= (data[j]**powers[i][j])

	# 	result.append(temp*coef[i])
	# return (sum(result)+ intercept)

def computeData():
	data=getData()
	for i in tqdm(range(1), desc="Getting Weights of Model"):
		coef, intercept= LinModel().getWeights()
	pk=data['public_key']
	pubkey= paillier.PaillierPublicKey(n=int(pk['n']))
	enc_data = []
	len_data = len(list(data['values']))
	for i in tqdm(range(len_data), desc="Loading Encrypted Data"):
		for i in data['values']:
			enc_data.append(paillier.EncryptedNumber(pubkey, int(i[0], int(i[1]))))
	for i in tqdm(range(len(coef)), desc="Computing Encrypted Prediction"):
		predict = []
		for i in range(len(coef)):
			predict.append(coef[i]*enc_data[i])
		results = sum(predict)+intercept
	return results, pubkey

def serializeData():
	results, pubkey = computeData()
	encrypted_data={}
	encrypted_data['pubkey'] = {'n': pubkey.n}
	encrypted_data['values'] = (str(results.ciphertext()), results.exponent)
	serialized = json.dumps(encrypted_data)
	return serialized

def getUnEncryptedPrediction():
	data = [0,1,2,1,640]
	coef, intercept= LinModel().getWeights()
	for i in tqdm(range(1), desc="Computing UnEncrypted Prediction"):
		result = sum([coef[i]*data[i] for i in range(len(coef))])+intercept
	return result

def main():
	for i in tqdm(range(1), desc="Serializing Encrypted Data Prediction"):
		datafile=serializeData()
		with open('enc_prediction.json', 'w') as file:
			json.dump(datafile, file)
	

if __name__=='__main__':
	main()

