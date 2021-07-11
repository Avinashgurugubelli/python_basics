from flask import Blueprint, request

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/', methods=("GET", "POST"))
def root():
    if request.method == 'POST':
        return "Employee Posted successfully"
    return "Employee Blue Print"

# @employee_bp.route('/', methods=["POST"])
# def root():
#     return "Employee Posted successfully"