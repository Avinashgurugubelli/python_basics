from flask import Flask, app
from flask_restful import Api
from blue_prints import employee_blue_print, root__blue_print

# Custom imports
from controllers.employee_controller import EmployeeController, EmployeesController


app: Flask = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# regestering controllers
api.add_resource(EmployeesController, '/api/v1/employees_controller', methods=['GET', 'POST'])
api.add_resource(EmployeeController, '/api/v1/employees_controller/<int:id>', methods=['GET', 'PUT', 'DELETE'])

# regestering blueprints
app.register_blueprint(root__blue_print.root_bp, url_prefix='/api/v1')
app.register_blueprint(employee_blue_print.employee_bp, url_prefix='/api/v1/employees')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6111)
