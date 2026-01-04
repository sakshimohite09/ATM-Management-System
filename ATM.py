class Atm:
    #Constructor
    counter =1 #Static variable

    def __init__(self):
        self.__pin=""   # Making private variable by giving double underscore before variable name
        self.__balance=0
        self.menu()
        self.sno =Atm.counter #Static variable is accessed inside constructor by using class name
        Atm.counter = Atm.counter + 1

    def menu(self):
            user_input = input("""
                            Hello, how would you like to proceed?
                            1.Enter 1 to creat pin
                            2.Enter 2 to deposit
                            3.Enter 3 to withdraw
                            4.Enter 4 to check balance
                            5.Enter 5 to exit
                        """)

            if user_input =="1":
                self.create_pin()
            elif user_input =="2":
                self.deposit()
            elif user_input =="3":
                self.withdraw()
            elif user_input =="4":
                self.check_balance()
            else:
                print("Bye")
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self._pin = new_pin
            print("Pin changed..")
        else:
            print("Not allowed..")
    
    def create_pin(self):
        self.__pin =input("Enter your pin:")
        print("Pin set successful..") 
        self.menu()  
    
    def deposit(self):
        temp =input("Enter your pin:")
        if temp == self.__pin:
            amount =int(input("Enter the amount:"))
            self.__balance =self.__balance + amount
            print("Deposit successful..")
        else:
            print("Invalid pin")
        self.menu()  
    
    def withdraw(self):
        temp =input("Enter your pin:")
        if temp == self.__pin:
            amount =int(input("Enter the amount:"))
            if amount <self.__balance:
                self.__balance =self.__balance - amount
                print("Operation successful..")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")
        self.menu()    
    
    def check_balance(self):
        temp = input("Enter your pin:")
        if temp ==self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin..") 

c1 = Atm()
c2 = Atm()
c3 = Atm()

print(c1.sno)
print(c2.sno)

Sbi = Atm()    #Sbi is reference variable
print(Sbi.menu())
print(Sbi.get_pin())
print(Sbi.set_pin("209807"))
