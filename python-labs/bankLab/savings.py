from BankAccInheritance import BankAcctInheritance


class Savings(BankAcctInheritance):
    MAX_DEPOSIT = 9_999

    def __init__(self, acctHolder, initBalance):
        super().__init__(acctHolder, initBalance)
        self._num_deposits = 0

    # Override make_deposit to allow for check on deposit amount
    def make_deposit(self, dep_amt):
        # Can't allow deposits > 9_999
        if dep_amt > 9_999:
            print(
                f'Deposit amount of {dep_amt} exceeds max ({Savings.MAX_DEPOSIT}) for this type of account')
            print('Deposit not done; balance unchanged')
        else:
            super().make_deposit(dep_amt)
            # Up # deposits
            self._num_deposits += 1

    def __str__(self):
        return (f'{"*" * 50}\nAccount type: {type(self).__name__}\n{super().__str__()}\n'
                f'Num deposits: {self._num_deposits}\n{50 * "*"}')
