from flask import jsonify
from flask_restful import Resource, request
from models.employee_model import EmployeeModel
from flask_inputs.validators import JsonSchema
from flask_inputs import Inputs

from repositories.employee_repo import EmployeeRepo
from schemas.employee_schema import employee_schema


class EmployeeSchemaValidator(Inputs):
    json = [JsonSchema(schema=employee_schema)]

class EmployeeController(Resource):
    def __init__(self) -> None:
        self.repo = EmployeeRepo()
    
    def get(self, id: int):
        print("GET ID: " + str(id))
        return self.repo.get_employee_by_id(id)

    def put(self, id: int):
        print("PUT ID: " + str(id))
        schema_validator = EmployeeSchemaValidator(request)
        if not schema_validator.validate():
            return jsonify(success=False, errors=schema_validator.errors)
        return self.repo.update_employee_by_id(id, request.get_json(force=True))

    def delete(self, id: int):
        print("DELETE ID: " + str(id))
        return self.repo.delete_employee_by_id(id)


class EmployeesController(Resource):

    def __init__(self) -> None:
        self.repo = EmployeeRepo()

    def get(self):
        name: str = request.args.get('name')
        email: str = request.args.get('email')
        if not name and not email:
            return self.repo.get_all_employees()
        else:
            return self.repo.search_employee(name, email)

    def post(self):
        print("POST ID: " + str(id))
        schema_validator = EmployeeSchemaValidator(request)
        if not schema_validator.validate():
            return jsonify(success=False, errors=schema_validator.errors)
        return self.repo.add_employee(request.get_json(force=True))
