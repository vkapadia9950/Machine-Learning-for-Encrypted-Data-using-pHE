import phe as paillier
import json

def storeKeys():
    public_key, private_key = paillier.generate_paillier_keypair()
    keys={}
    keys['public_key'] = {'n': public_key.n}
    keys['private_key'] = {'p': private_key.p,'q':private_key.q}
    with open('keypair.json', 'w') as file: 
    	json.dump(keys, file)

if __name__=='__main__':
    storeKeys()