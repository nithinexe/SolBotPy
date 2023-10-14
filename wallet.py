from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solders.system_program import TransferParams, transfer

import json

solana_client = Client("https://api.devnet.solana.com")

def create_account(sender_username):
    try:
        # Your code here
        kp = Keypair.generate()
        public_key = str(kp.public_key)
        secret_key = kp.secret_key

        data = {
            'public_key': public_key,
            'secret_key': secret_key.decode("latin-1"),
        }

        file_name = '{}.txt'.format(sender_username)
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)


        return public_key
    except Exception as e:
        print('error:', e)
        return None
    
def load_wallet(sender_username):
    try:
        file_name = '{}.txt'.format(sender_username)
        with open(file_name) as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print('error:', e)
        return None
 
def fund_account(sender_username, amount):
    try:
        amount = int(1000000000 * amount)
        account = load_wallet(sender_username)
        resp = solana_client.request_airdrop(
            account['public_key'], amount)   
        print(resp)    

        transaction_id = resp['result']
        if transaction_id != None:
            return transaction_id
        else:
            return None

    except Exception as e:
        print('error:', e)
        return None
    

       