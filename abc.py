from abc import ABC, abstractmethod

class payment(ABC):
  @abstractmethod
  def showpayment(self, amount):
    pass

class creditcardpay(payment):
  def showpayment(self,amount):
    print(f"amount {amount} sent using credit card")

class easypaisapay(payment):
  def showpayment(self, amount):
    print(f"payment succeed of amount {amount} via easypaisa")

card = creditcardpay()
easy = easypaisapay()


card.showpayment(15000)
easy.showpayment(3000)
