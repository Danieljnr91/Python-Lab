# class Student:
#   def __init__(self,name,age):
#     self.__name=name
#     self.__age=age
#   def get_name(self):
#     return self.__name
#   def get_age(self):
#     return self.__age
#   def set_name(self,new_name):
#     self.__name = new_name
#     return self.__name
#   def set_age(self,new_age):
#     if new_age < 0:
#       return "Invalid"
#     else:
#       self.__age = new_age
#       return self.__age
    
# obj = Student("LAD",23)
# print(obj.get_name())
# print(obj.get_age())
# print(obj.set_name("Luke"))
# print(obj.set_age(34))



class BankAccount:
  def __init__(self,owner,balance,pin):
    self.__name=owner
    self.__balance=balance
    self.__pin=pin
  def get_owner(self):
    return f"{self.__name} is the owner of the account"
  def get_balance(self):
      return f"${self.__balance} is the amount in your account"
  def set_owner(self,new_name):
    self.__name=new_name
    return f"Account name has been changed to {self.__name}"
  def set_balance(self,pin,withdraw_amt,deposit_amt,choice):
    if choice==1:
      self.__balance+=deposit_amt
      return f"${deposit_amt} has been added to your account, balance is now ${self.__balance}"
    elif choice == 2:
      self.__balance-=withdraw_amt
      return f"${withdraw_amt} has been deducted from your account, balance is now {self.__balance}"
      
  def set_pin(self,old_pin,new_pin):
    if self.__pin!=old_pin:
      return f"Enter your previous pin correctly"
    else:
      self.__pin = new_pin
      return "Your Pin has been updated"

name = input("Enter name:")
balance = float(input("Enter Balance:"))
pin = int(input("Set Account Pin:"))
bank_obj = BankAccount(name,balance,pin)
print(bank_obj.get_owner())
print(bank_obj.get_balance())
print("CHOOSE OPERATION: \n1.Change account name \n2.Edit account balance \n3.Change account Pin")
while True:
  ops = input("Choose(1/2/3):")
  if ops=="1":
    new_name = input("Enter new name:")
    print(bank_obj.set_owner(new_name))
  elif ops=="2":
    pin = int(input("Enter pin:"))
    if pin != bank_obj._BankAccount__pin:
      print("INVALID PIN")
    else:
      print("Enter: \n1.To Deposit \n2.To Withdraw")
      choice = int(input("Choose:"))
      if choice == 1:
        dep_amt = float(input("Enter amount to deposit:"))
        print(bank_obj.set_balance(pin=pin,withdraw_amt=0,deposit_amt=dep_amt,choice=1))
      else:
        with_amt = float(input("Enter amount to withdraw:"))
        print(bank_obj.set_balance(pin=pin,withdraw_amt=with_amt,deposit_amt=0,choice=2))
  else:
    old_pin =int(input("Enter old Pin"))
    new_pin = int(input("Enter new pin:"))
    print(bank_obj.set_pin(old_pin,new_pin))
     
