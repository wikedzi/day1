from abc import ABCMeta, abstractmethod
import time

class Account(metaclass=ABCMeta):
   'This is an Abstract class that defines all the necessary features of a Bank account'

   def getAccountCreationDate(self):
       raise NotImplementedError()

   def getAccountNumber(self):
       raise NotImplementedError()

   def withdraw(self):
       raise NotImplementedError()

#Start of Saving Account class
class Saving(Account): # Saving is an Account
   __accountsCreated = 0 # using the __ to encapsulate the data
   def __init__(self, aName, aNumber, initialdeposit):
      self.accNname = aName
      self.accNumber = aNumber
      self.accCreatedAt = time.time()
      self.accBalance = initialdeposit
      Saving.__accountsCreated += 1
   def getBalance(self):
      return self.accBalance

   def getAccountCreationDate(self):
      return self.accCreatedAt

   def getAccountNumber(self):
      return self.accNumber

   def deposit(self,amount):
      if (type(amount) is float or type(amount) is int) and amount > 0:
         self.accBalance += amount;
      else:
         return "Please check the amount you have specifies to see it meets the requirements of being a Decimal number"
      return " New balance is " + str(self.accBalance)   

   def withdraw(self, amount):
      if self.accBalance > amount:
         self.accBalance -= amount
      else:
         return "Insufficient balance to withdraw " + str(amount)
      return self.accNumber

#Fixed Account class
class Fixed(Account): # Fixed is an Account
   __accountsCreated = 0 # using the __ to encapsulate the data
   __interest = 0;
   def __init__(self, aName, aNumber, fAmount, fTerm, aInterest):
      self.accNname = aName
      self.accNumber = aNumber
      self.accCreatedAt = time.time()
      self.accBalance = 0
      self.fixedAMount = fAmount
      self.fixedTerm = fTerm
      self.__interest = aInterest #given in percentage (1 to 100)
      Fixed.__accountsCreated += 1

   def getBalance(self):
      return self.fixedAMount * (1 + self.__interest)

   def getFixedAmount(self):
      return self.fixedAMount

   def getAccountCreationDate(self):
      return self.accCreatedAt

   def getAccountNumber(self):
      return self.accNumber   

   def withdraw(self):
      #since it is fixed account,we dont withdraw partial amounts, we besically take everything out 
      # it is important that we check if the balance has matured
      today = time.time();
      maturity_time = self.fixedTerm * 24 * 60 * 60# we find the number of seconds that are eqaul to fixedTerm
      if today - self.accCreatedAt < maturity_time :
         return "The investiment is not yet matured"

      amount = self.getBalance();
      self.accBalance = 0;
      return str(amount) + " has been successfully withdrawn"

#Run tests
account = Saving("Timothy Wikedzi","0756556616",2000)
print(account.getBalance())
account.deposit(430)
print(account.getBalance())

#run tests for a fixed account
print("----------------Fixed account---------")
account = Fixed("Gladness Wikedzi","0754556616",2000,365,0.5)
print(account.getBalance())
print(account.withdraw())