from savings import Savings
from checkings import Checking

# Create some accounts
accts = [Savings("saHolder1", 123_456), Checking("chHolder1", 34_456), Savings("holder2", -234),
         Savings("saHolder3", 23_456), Checking("chHolder2", 4_456), Checking("chholder3", 234)]
# Print accts[0] (a Savings acct) and accts[1] (a Checking account)
print(f'{accts[0]}\n{accts[1]}')
# Deposit 15_000 in a accts[0]; reprint account
accts[0].make_deposit(15_000)
print(accts[0])
# Deposit 5_000 in a accts[0]; reprint account
accts[0].make_deposit(5_000)
print(accts[0])
# Withdraw 2_000 in accts[1]; reprint account
accts[1].make_withdrawal(2_000)
print(accts[1])
