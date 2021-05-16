import time

from substrateinterface import SubstrateInterface, Keypair



def create_substrate_wallet():
    mnemonic = Keypair.generate_mnemonic()
    keypair = Keypair.create_from_mnemonic(mnemonic)
    data_ = {
        'address': keypair.ss58_address,
        'mnemonic': mnemonic,
        'publicKey': keypair.public_key,
        'privateKey': keypair.private_key,
        'ss58Format': keypair.ss58_format,
        'cryptoType': keypair.crypto_type
    }
    return data_

def create_eth_wallet():
    current_time = str(int(time.time()))
    new_wallet = web3.geth.personal.new_account('the-passphrase')
    data_ = {
        'address': new_wallet.address,
        'key': new_wallet.key
    }
    return data_