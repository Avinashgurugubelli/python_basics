from db.my_sql_db_context import MySqlDbContext
from models.employee_model import EmployeeModel

class EmployeeRepo:
    
    def __init__(self) -> None:
        self.__db_context = MySqlDbContext()
    
    def get_all_employees(self):
        return self.__db_context.select("SELECT * FROM employees")
    
    def get_employee_by_id(self, id: int):
        return self.__db_context.select("SELECT * FROM employees where id=" + str(id))
    
    def update_employee_by_id(self, id: int, payload: EmployeeModel):
        return self.__db_context.fire_query("UPDATE employees SET name='" + payload.name + "',email_id='" + payload.email_id + "',phone_number='" + payload.phone_number + "' WHERE id=" + id)
    
    def delete_employee_by_id(self, id: int):
        return self.__db_context.fire_query("DELETE FROM employees WHERE id =" + id)
    
    def add_employee(self, payload: EmployeeModel):
        return self.__db_context.fire_query("INSERT INTO employees (id, name, email_id, phone_number) VALUES (" + payload.id + ",'" + payload.name + "','" + payload.email_id + "','" + payload.phone_number + "')")
        
    def search_employee(self, name: str, email_id: str):
        return self.__db_context.select("SELECT * FROM employees WHERE name='" + name + "' or email_id='" + email_id + "'")