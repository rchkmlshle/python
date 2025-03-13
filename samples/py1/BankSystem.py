
"""
You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].

Execute all the valid transactions. A transaction is valid if:

The given account number(s) are between 1 and n, and
The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
Implement the Bank class:

Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.
"""
from typing import List  

class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.N = len(self.balance)
    
    def transfer(self, account1: int, account2:int, money:int) -> bool:
        account1 -= 1
        account2 -= 1
        if account1 < self.N and account2 < self.N:
            if money <=self.balance[account1]:
                self.balance[account1] -=money
                self.balance[account2] += money
                return True
            return False
        return False
    
    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if account < self.N:
            self.balance[account] += money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if account < self.N and self.balance[account] >= money:
            self.balance[account] -= money
            return True
        return False

def main():
    action=["Bank","withdraw","transfer","deposit","transfer","withdraw"]
    bal=(
        [[10,100,20,50,30],
         [3,10],
         [5,1,20],
         [5,20],
         [3,4,15],
         [10,50]])

    sln1=Bank(bal[0])

    print(

    sln1.withdraw(bal[1][0], bal[1][1]),
    sln1.transfer(bal[2][0] , bal[2][1], bal[2][2]),
    sln1.deposit(bal[3][0], bal[3][1]),
    sln1.transfer(bal[4][0], bal[4][1], bal[4][2]),
    sln1.withdraw(bal[5][0], bal[5][1])
    )


if __name__=='__main__':
    main()