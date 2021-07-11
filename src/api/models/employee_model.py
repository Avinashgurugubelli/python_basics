'''
Module EmployeeModel
defines an entity class Employee
'''

class EmployeeModel:
    def __init__(self, id: int, name: str, email_id: str, phone_number: str) -> None:
        self.__id = id
        self.__name = name
        self.__email_id = email_id
        self.__phone_number = phone_number
    
    # Getters
    @property
    def id(self)-> int:
        return self.__id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def email_id(self)-> str:
        return self.__email_id
    
    @property
    def phone_number(self)-> str:
        return self.__phone_number
    
    # Setters
    @phone_number.setter
    def phone_number(self, phone_number: str):
        self.__phone_number = phone_number
    
    @email_id.setter
    def email_id(self, email_id: str):
        self.__email_id = email_id
    


