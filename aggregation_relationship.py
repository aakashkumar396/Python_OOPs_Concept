#Aggregation Relationship
"""
The relationship between the object and its static variable is nothing but aggreggation,
In python it is Has-A. Its a one-way relationship.
In below code Customer "HAS-A"  name and adress
"""



class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_details(self,new_name,new_city,new_pincode,new_state):
        self.name = new_name

        #calling new_address method from Address class for changes
        self.address.new_address(new_city,new_pincode,new_state)
    


class Address:
    def __init__(self,city, pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def new_address(self,new_city,new_pincode,new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state    

add = Address("New Delhi",110074,"Delhi")
cust = Customer("Aakash","Male",add)


cust.edit_details("Kumar","Gurugram",112839,"Haryana")

print(cust.address.pincode)
#print(cust.address.city)
#print(cust.address.state)
