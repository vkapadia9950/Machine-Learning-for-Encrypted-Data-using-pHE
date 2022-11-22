import phe as paillier
import json
import os
from tqdm import tqdm
from server import getUnEncryptedPrediction

def getKeys():
    for i in tqdm(range(1), desc="Generating Keys"):
        os.system("python generate_key.py")
    print("-------------------------------------")
    print("NEW PUBLIC AND PRIVATE KEYS AVAILABLE")
    print("-------------------------------------")
    with open('keypair.json', 'r') as file: 
        keys=json.load(file)
        pub_key=paillier.PaillierPublicKey(n=int(keys['public_key']['n']))
        priv_key=paillier.PaillierPrivateKey(pub_key,keys['private_key']['p'],keys['private_key']['q'])
        return pub_key, priv_key 

def serializeData(public_key, data):
	encrypted_data_list = [public_key.encrypt(x) for x in data]
	encrypted_data={}
	encrypted_data['public_key'] = {'n': public_key.n}
	encrypted_data['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_data_list]
	serialized = json.dumps(encrypted_data)
	return serialized

def loadAnswer():
    with open('enc_prediction.json', 'r') as file: 
    	ans=json.load(file)
    answer=json.loads(ans)
    return answer


def sendData(pub_key):
    data = [0,1,2,1,640]
    datafile = serializeData(pub_key,data)
    with open('enc_data.json', 'w') as file:
        json.dump(datafile, file)

def load(pub_key, priv_key):
    answer_file = loadAnswer()
    answer_key = paillier.PaillierPublicKey(n=int(answer_file['pubkey']['n']))
    answer = paillier.EncryptedNumber(answer_key, int(answer_file['values'][0]), int(answer_file['values'][1]))
    if answer_key == pub_key:
        return "Result of prediction with encryption "+ str(priv_key.decrypt(answer))
    else:
        return "Incorrect key"

pub_key, priv_key = getKeys()

print("[S]END DATA")
print("[P]REDICT RESULT")
print("[L]OAD RESULT")
print("[U]NENCRYPTED RESULT")
print("CHOOSE OPERATION")
s = input()

while s == 'S' or s == 'P' or s == 'L' or s == "U":
    if s == "S":
        for i in tqdm(range(1), desc="Sending Encrypted Data"):
            sendData(pub_key)
        print("---------")
        print("DATA SENT")
        print("---------")
    elif s == "L":
        for i in tqdm(range(1), desc="Loading Result"):
            ans = load(pub_key, priv_key)
        print("------------------------------")
        print(ans)
        print("\n")
        print("RESULT OF ENCRYPED DATA LOADED")
        print("------------------------------")
    elif s == 'P':
        for i in tqdm(range(1), desc="Getting Prediction for Encrypted Data"):
            os.system("python server.py")
        print("----------------------------------")
        print("ENCRYPTED DATA PREDICTION RECEIVED")
        print("----------------------------------")
    elif s == "U":
        for i in tqdm(range(1), desc="Getting Prediction for UnEncrypted Data"):
            result = getUnEncryptedPrediction()
        print("------------------------------------")
        print("Result of prediction without encryption", result)
        print("\n")
        print("UNENCRYPTED DATA PREDICTION RECEIVED")
        print("------------------------------------")
        break
    print("[S]END DATA")
    print("[P]REDICT RESULT")
    print("[L]OAD RESULT")
    print("[U]NENCRYPTED RESULT")
    print("CHOOSE OPERATION")
    s = input()