from datetime import datetime


class BankAcctInheritance:

    last_acct_id = 1

    def __init__(self, acct_holder, init_balance):
        self._acct_ID = BankAcctInheritance.last_acct_id
        BankAcctInheritance.last_acct_id += 1

        self._acct_holder = acct_holder
        self._date_opened = datetime.now()

        if init_balance < 0:
            print(
                F"Invalid initial balance amount {init_balance}. Initial balance set to 0")
            init_balance = 0

        self.balance = init_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_bal):
        if 0 <= new_bal:
            self._balance = new_bal
        else:
            print(f'Value {new_bal} invalid for balance field; no change made')

    # Make a deposit - keep it simple
    def make_deposit(self, dep_amt):
        if 0 < dep_amt:
            self.balance += dep_amt
        else:
            print(
                f'Value {dep_amt} invalid for deposit amount; no change made')

    # Make a withdrawal - overdrafts allowed
    def make_withdrawal(self, with_amt):
        if 0 < with_amt:
            self.balance -= with_amt
        else:
            print(
                f'Value {with_amt} invalid for withdrawal amount; no change made')

    # Print account particulars
    def __str__(self):
        return (f'Account info for account ID: {self._acct_ID}\n'
                f'Holder: {self._acct_holder}\tDate opened: {self._date_opened}\tBalance: {self.balance:,}')
