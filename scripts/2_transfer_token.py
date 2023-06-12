from brownie import OurToken, accounts, config
from scripts.helpful_scripts import get_account

def read_contract():
    mytoken = OurToken[-1]
    account = get_account()
    print(account)
    transaction = mytoken.transfer("0x1c4488ACC83fD5578B633e844B97e98E56d57B1d",2000000000000000000, {"from": account}) 
    transaction.wait(1)
    print(transaction)

def main():
    read_contract()