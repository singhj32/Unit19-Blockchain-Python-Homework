import os
import subprocess
import json
from web3 import Web3
from eth_account import Account


from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from constants import *

from web3.middleware import geth_poa_middleware




mnemonic = os.getenv('MNEMONIC')

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def derive_wallets(MNEMONIC,whichcoin,numderive):
    command = 'php ./hd-wallet-derive.php -g --mnemonic="' + MNEMONIC + '" --cols=path,address,privkey,pubkey --coin="' + whichcoin + '" --numderive="' + str(numderive) + '" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()

    keys = json.loads(output)
    return (keys)

def priv_key_to_account(coin, priv_key):
    if coin=='eth':
        return(Account.privateKeyToAccount(priv_key))
        #return (w3.eth.accounts.privateKeyToAccount(priv_key))
    elif coin=='btc-test':
        return (PrivateKeyTestnet(priv_key))

def create_tx(coin, account, to, amount):
    if coin=='eth':
        gasEstimate = w3.eth.estimateGas({"from": account.address, "to": to, "value": amount})
        return { "from": account.address,"to": to,"value": amount,"gas": gasEstimate, "gasPrice": w3.eth.gasPrice,"nonce": w3.eth.getTransactionCount(account.address)}
    elif coin=='btc-test':
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(tx)
    if coin=='eth':
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return result.hex()
    elif coin=='btc-test':
        return NetworkAPI.broadcast_tx_testnet(signed_tx)  
                
        

        
        
        
