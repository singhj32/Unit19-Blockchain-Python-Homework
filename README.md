# Creating Multi-Blockchain Wallet in Python
<p align="center">
<img src="./images/newtons-coin-cradle.jpg?raw=true" alt="Sublime's custom image"/>
</p>

We'll use the following tools to create/access the blockchain network and conduct transactions:

1. **hd-wallet-derive** - to generate wallet addresses.
2. **Python libraties (bit and web3)** - to create account objects and conduct transactions.
3. **Mycrypto tool** - to conduct initial ethereum transaction.
4. **Online tools** - to fund bitcoin and check transaction status.
<br>
<br>

We will write python code to generate wallets and conduct transactions. Full python code can be found in  "./hd-wallet-derive/wallet.py" file.

## **_Using hd-wallet-derive to derive wallets and addresses:_**
We are using python code is to derive wallets from our mnemonic phrase. The function below derives wallets and returns the addresses, public keys and private keys associated with them. **hd-wallet-derive.php** command needs a 12 length mnemonic that we provide as a parameter to the funtion when calling it. The funtion also takes coin and numdrive parameters that are used to derive wallets for a particular coin and tell the command how many addresses we need it to generate. The command when used with "--format=json" swith can return the data in JSON format which can further be transformed in to a list of dictionary items as shown below. Custom code can then be written to extract the address and keys from this list.

**Function:**

    def derive_wallets(MNEMONIC,whichcoin,numderive):
      command = 'php ./hd-wallet-derive.php -g --mnemonic="' + MNEMONIC + '" --cols=path,address,privkey,pubkey --coin="' + whichcoin + '" --numderive="' + str(numderive) + '" --format=json'
      p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()

      keys = json.loads(output)
      return (keys)
**Output:**

      [{'path': "m/44'/1'/0'/0/0",
      'address': 'mmC3sCD1yNXPREZPwtReSeuA8VRVV9bg87',
      'privkey': 'XXXXXXNSNTZ7KttgAb8Lmbx6crGCXhFwveijd1MVXXXXXXXX',
      'pubkey': '02f52b5ad9b367236825d4fdaeeeb2dab5215456856342d53c3688d2100e4c5bb4'},
      {'path': "m/44'/1'/0'/0/1",
      'address': 'mqsdD5qYzntqwncB9mNxfmXXukDQuwNWHX',
      'privkey': 'xxxxxxxxxxsVqFGfS1KR24pKPhKFPViobchHiTuAxxxxxxxxxx23',
      'pubkey': '0287e5ae34b411fe9dff7ccb50cfff5aa6d8d17c9bff55121cb84943fa58c0b8d3'},
      {'path': "m/44'/1'/0'/0/2",
      'address': 'mxy9bvy7iWGsSwUuMaekWsxMZbaFbpcLeu',
      'privkey': 'zzzzzzzzzzGwF7RADoBrXjsHkvMEY7s63SdkveFzzzzzzzzzzzX',
      'pubkey': '033308e7ddb0bdd8fa382c03929aaa85fc3543dbd29398c688d5aa13636714b871'}]


      


**hd-wallet-derive** installation instructions can be found here:

* [hd-wallet-derive installation instructions](https://github.com/dan-da/hd-wallet-derive/blob/master/README.md)

* [hd-wallet-derive github respository](https://github.com/dan-da/hd-wallet-derive)

 * [installation instructions video](https://www.youtube.com/watch?v=A_tqm4j4vsY&feature=youtu.be) 
<br>

## **_Generate accounts from the private keys using python:_**
 We call the below function to create account objects for specific coins. We used the python console to copy the keys manually and use them while calling the funtions but custom code can be written to extract the private keys from the derived wallets and pass on to below funtion.

      
    def priv_key_to_account(coin, priv_key):
      if coin=='eth'
         return(Account.privateKeyToAccount(priv_key))
      elif coin=='btc-test':
      return (PrivateKeyTestnet(priv_key))   
  

<p align="center">
<img src="./images/accountcreation.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>

## **_Send transactions from pyhton:_**
   We use the below code to create and send transactions for "eth" and "btctest". 

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

### **_Send "ETH" transaction and check status:_**

 First we need to run the local blockchain using puppeth and geth commands. Then make a transaction using mycrypto to workaround the web3 library bug mentioned in the instructions. Finally, we send the actual transaction to the network.

 Ethereum block chain nodes:
 <p align="center">
<img src="./images/eth_nodes.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>

Sending ethereum transaction:
<p align="center">
<img src="./images/ethtransaction.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>
 
Checking ethereum transaction status:
<p align="center">
<img src="./images/eth_transaction_status.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>

### **_Send "BTC" transaction and check status:_**

 Create btc account and send transaction as follows. Check the transaction status online.



Sending BTC transaction:
<p align="center">
<img src="./images/btctransaction.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>
 
Checking BTC transaction status:
<p align="center">
<img src="./images/btc_transaction_status.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>

**Conclusion:** Python libraries provides support for blockchain and crypto currencies and they can be used to write custom applications as needed. In the above demonstration, both btctest and ethereum transactions were successful. We can enhance the above application to perform transactions in other types of crypto currencies.