
class Person:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    
    def print_person1(self):
        print('Name', self.__name)
        print('Address:', self.__address)
        print('Phone:', self.__phone)
    
    


class Customer(Person):
    def __init__(self,name,address,phone,cust_number,mailing):

        Person.__init__(self, name, address, phone)
    
        self.__cust_number = cust_number
        self.__mailing = mailing 
    
    def print_person(self):
        print('Name:', self.__name)
        print('Address:', self.__address)
        print('Phone:', self.__phone)
        print('Customer number:', self.__cust_number)
        print('Mailing:', self.__mailing)
