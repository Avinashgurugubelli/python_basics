from db.my_sql_db_context import MySqlDbContext
from models.employee_model import EmployeeModel

class EmployeeRepo:
    
    def __init__(self) -> None:
        self.__db_context = MySqlDbContext()
    
    def get_all_employees(self):
        return self.__db_context.select("SELECT * FROM employees")
    
    def get_employee_by_id(self, id: int):
        return self.__db_context.select("SELECT * FROM employees where id=" + str(id))
    
    def update_employee_by_id(self, id: int, body: EmployeeModel):
        return "update Employee by id"
    
    def delete_employee_by_id(self, id: int):
        return "delete Employee by id"
    
    def add_employee(self, employee: EmployeeModel):
        return "Add Employee"
        
    def search_employee(self, name: str, email_id: str):
        return self.__db_context.select("SELECT * FROM employees WHERE name='" + name + "' or email_id='" + email_id + "'")