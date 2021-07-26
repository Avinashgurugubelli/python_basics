import json
from db.my_sql_db_context import MySqlDbContext
from models.employee_model import EmployeeModel

class EmployeeRepo:
    
    def __init__(self) -> None:
        self.__db_context = MySqlDbContext()
    
    def get_all_employees(self):
        return self.__db_context.select("SELECT * FROM employees")
    
    def get_employee_by_id(self, id: int):
        return self.__db_context.select("SELECT * FROM employees where id=" + str(id))
    
    def update_employee_by_id(self, id: int, payload):
        query = "UPDATE employees SET name='{}',email_id='{}',phone_number='{}' WHERE id={}".format(payload['name'],  payload['email_id'], payload['phone_number'], id)
        return self.__db_context.fire_query(query=query)
    
    def delete_employee_by_id(self, id: int):
        query = "DELETE FROM employees WHERE id ={}".format(id)
        return self.__db_context.fire_query(query=query)
    
    def add_employee(self, payload):
        query = "INSERT INTO employees (id, name, email_id, phone_number) VALUES({}, '{}', '{}', '{}')".format(payload['id'], payload['name'],  payload['email_id'], payload['phone_number'])
        return self.__db_context.fire_query(query=query)
        
    def search_employee(self, name: str, email_id: str):
        return self.__db_context.select("SELECT * FROM employees WHERE name='" + name + "' or email_id='" + email_id + "'")