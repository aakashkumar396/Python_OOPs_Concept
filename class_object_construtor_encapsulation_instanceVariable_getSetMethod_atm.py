
class Atm:

    #static/class variable-> same variable value for all method/attribute. Always written outside constructor
    __counter = 1
    
    #constructor
    def __init__(self):

        #Encapsulation -> it is used to hide unnecessary details from user
        
        #instance variable -> The values of these variable are different for each method
        self.__pin = ""         #syntax for encapsulation   #Drawback => data hiding in python truely not possible    
        self.__balance = 0      #To access hidden data variable details, the syntax is => objectName._className__attribute/methodName =>example -- sbi._Atm__pin/balance

        self.sno = Atm.counter              #sysntax for calling static variable into constructor.
        Atm.__counter = Atm.__counter + 1        #it will increase customer serial number as per entry
        
        #self.__menu()

    #Get & Set method => if user want to access private data and do some modifcation but it is only happen via default logic which is already declared

    @staticmethod
    def get_counter():          #there is no self keyword because we are returning via Function keyword
        return Atm.__counter
    @staticmethod
    def set_counter(new):
        if (type(new)) == int:
            Atm.__counter = new
        else:
            print("Invalid Type.")
        

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("PIN changed")
        else:
            print("Invalid Pin Type")

    #menu function
    def __menu(self):
        user_input = input("""
                    1. Create PIN
                    2. Amount Deposit
                    3. Check Balance
                    4. Withdrawl Amount
                    5. Exit
""")
        if user_input == "1":
            self.pin_creation()
        elif user_input == "2":
            self.amount_deposit()
        elif user_input == "3":
            self.balance()
        elif user_input == "4":
            self.withdrawl()
        else:
            print("Time Out")


    #PIN Creation method
    def pin_creation(self):
        self.__pin = input("Enter new pin : ")
        print("PIN successfully created....")

    #Amount Deposit method
    def amount_deposit(self):
        temp= input("Enter PIN ")
        if temp == self.__pin:
            amount = int(input("Enter amount to deposit :"))
            self.__balance = self.__balance + amount
            print("Amount Deposited Successfully.....")
        else:
            print("Invalid PIN...")

    #Balance CHecking
    def check_balance(self):
        temp = input("Enter PIN : ")
        if temp == self.__pin:
            print("Total amount : ",self.__balance)
        else:
            print("Invalid PIN")
    
    #Amount withdrawl
    def check_withdrawl(self):
        temp = input("Enter PIN : ")
        if temp == self.__pin:
            amount = int(input("Enter Amount to be withdrawl :"))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Withdrawl Succesfully")
                print("Total amount left", self.balance)
            else:
                print("insufficient amount")
        else:
            print("Invalid PIN....")



            


