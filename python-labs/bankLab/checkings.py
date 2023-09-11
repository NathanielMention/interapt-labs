from BankAccInheritance import BankAcctInheritance


class Checking(BankAcctInheritance):

    NSF_FEE = 35

    def __init__(self, acctHolder, initBalance):
        super().__init__(acctHolder, initBalance)
        self._num_withdrawals = 0

    # Override make_withdrawal to allow for NSF charge on overdraft
    def make_withdrawal(self, with_amt):
        super().make_withdrawal(with_amt)
        # Check for overdraft; apply NSF charge if so
        if self.balance < 0:
            self.balance -= Checking.NSF_FEE
        # Up # withdrawals
        self._num_withdrawals += 1

    def __str__(self):
        return (f'{"*" * 50}\nAccount type: {type(self).__name__}\n{super().__str__()}\n'
                f'Num withdrawals: {self._num_withdrawals}\n{50 * "*"}')
