class computer:
  def __init__(self):
    self.__maxprice=900


  def sell(self):
    print("Selling price=",self.__maxprice)


c=computer()
c.sell()

c.__maxprice=1000
c.sell()