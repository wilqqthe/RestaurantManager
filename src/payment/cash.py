
class Cash:
    cash_state = 0
    card_state = 0

    @classmethod
    def addCashPayment(cls, value):
        cls.cash_state += value

    @classmethod
    def addCardPayment(cls, value):
        cls.card_state += value