# Creating Multi-Blockchain Wallet in Python
<p align="center">
<img src="./images/newtons-coin-cradle.jpg?raw=true" alt="Sublime's custom image"/>
</p>

We'll use the following tools to create the blockchain network:

1. hd-wallet-derive - to generate wallet addresses.
2. Python libraties bit and web3 - to create account objects and conduct transactions.
3. Mycrypto - to conduct initial ethereum transaction.
4. Online tools - to fund bitcoin and check transaction status.
<br>
<br>

We will write python code to generate wallets and conduct transactions. Full python code can be found in "wallet.py" file.

## _Using hd-wallet-derive to derive wallets and addresses:_
Below code is called to derive the wallets. The function below derives wallets and returns the addresses, public keys and private keys associated with them. "hd-wallet-derive.php" command needs a 12 length mnemonic that you we provide as a parameter to the funtion when calling it. This funtion also takes the coin and numdrive parameters that are used to derive wallets for a particular coin and tell the command how many addresses we need it to generate.

      
    def derive_wallets(MNEMONIC,whichcoin,numderive):
      command = 'php ./hd-wallet-derive.php -g --mnemonic="' + MNEMONIC + '" --cols=path,address,privkey,pubkey --coin="' + whichcoin + '" --numderive="' + str(numderive) + '" --format=json'
      p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()

      keys = json.loads(output)
      return (keys)

<br>

## _Generating accounts from the private keys using python:_
 We call the below function to create account objects for specific coins. We used the python console to copy the keys and use them while calling the funtions but separate code can be written to extract the private keys from the derived wallets and pass on to below funtion.

      
    def priv_key_to_account(coin, priv_key):
      if coin=='eth'
         return(Account.privateKeyToAccount(priv_key))
      elif coin=='btc-test':
      return (PrivateKeyTestnet(priv_key))   
  

<p align="center">
<img src="./images/accountcreation.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>

## _Send transactions from pyhton:_
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

### _send "ETH" transaction and check status:_

 First we need to run the local blockchain using puppeth and geth commands. Then make a transaction using mycrypto to workaround the web3 library bug mentioned in the instructions. Then send the transaction.

 Ethereum block chain nodes:
 <p align="center">
<img src="./images/eth_nodes.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>

Sending Ethereum transaction:
<p align="center">
<img src="./images/ethtransaction.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>
 
Checking Ethereum transaction status:
<p align="center">
<img src="./images/eth_transaction_status.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>

### _send "BTC" transaction and check status:_

 First we need to run the local blockchain using puppeth and geth commands. Then make a transaction using mycrypto to workaround the web3 library bug mentioned in the instructions. Then send the transaction.



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