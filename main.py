from mnemonic import Mnemonic
import bitcoin
import bitcoinlib.keys
import requests
import json

mnemo = Mnemonic("english")   #get list with words, which create seed phrase

type = 'bitcoin'   #type of coin, which wallets you want get 
network = "BTC"   #for using API link

def generate_seed_phrase():
    seed = mnemo.generate(strength=128)   #generate seed phrase
    return seed

def generate_bitcoin_account():
    seed_phrase = generate_seed_phrase()
    private_key = mnemo.to_seed(seed_phrase)
    public_key = bitcoin.privtopub(private_key)
    p2pkh_address = bitcoin.pubtoaddr(public_key)
    p2sh_address = bitcoin.b58check_to_hex(bitcoin.pubtoaddr(public_key, 5))
    wif = bitcoinlib.keys.Key(network=type)
    wallet_important_format = wif.wif()
    account_info = {
        "type": type,
        "mnemonic": seed_phrase,
        "private_key": private_key.hex(),
        "public_key": public_key,
        "wallet_important_format": wallet_important_format
        "p2pkh_address": p2pkh_address,
        "p2sh_address": p2sh_address
    }
    return account_info

def get_transactions(address):
    try:
        response = requests.get(f"https://api.test.com/search?q={address}")
        """
        You need your OWN API of anything blockchain for
        checking transactions in wallet!
        """
        return response.json()
    except:
        print(f"Transactions on wallet {address} not found")
        return 0

if __name__ == "__main__":
    generate = True   #generete accounts, while script not detect transactions in wallet
    i = 0   #for counting generate accounts
    while(generate):
        print("#" + str(i + 1) + " account:")
        account_info = generate_bitcoin_account()
        
        print("Type (coin):", account_info["type"])
        print("Mnemonic:", account_info["mnemonic"])        
        print("Private Key:", account_info["private_key"])
        print("Public Key:", account_info["public_key"])
        print("Wallet Important Format (WIF):", account_info["wallet_important_format"])
        print("P2PKH Address:", account_info["p2pkh_address"])
        print("P2SH Address:", account_info["p2sh_address"])
        
        wif = account_info["wallet_important_format"]

        transactions = get_transactions(wif)   #get list of transactions in .json format
        if transactions != 0:
            for transaction in transactions:
                print(f"Transaction: {transaction}")
            
        print()
