import requests

import json

from requests.exceptions import HTTPError


class SampleRestClient:

    def __init__(self) -> None:
        self.base_url = 'http://localhost:6111/api/v1/employees_controller'

    def get_all_employees(self):
        try:
            response = requests.get(self.base_url)
            if response.status_code == 200:
                print("Employee details fetched successfully!")
                print(response.json())
            else:
                print("No data found")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def search_employee(self, name, email):
        try:
            query = {'name': name, 'email': email}
            response = requests.get(self.base_url, params=query)
            print(response.url)
            if response.status_code == 200:
                print("Employee details fetched successfully!")
                print(response.json())
            else:
                print("No matched found")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def get_employee_by_id(self, id: int):
        try:
            url = f'{self.base_url}/{str(id)}'
            response = requests.get(url)
            if response.status_code == 200:
                print("Employee details fetched successfully!")
                print(response.json())
            else:
                print("No matched found")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
    
    def delete_employee_by_id(self, id: int):
        try:
            url = f'{self.base_url}/{str(id)}'
            response = requests.delete(url)
            if response.status_code == 200:
                print("Employee deleted successfully!")
                print(response.json())
            else:
                print("Failed to delete")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def add_employee(self, employee):
        try:
            # print(employee)
            api_headers = {
                'content-Type': 'application/json',
                'accept': 'application/json'
            }
            response = requests.post(
                self.base_url, data=json.dumps(employee), headers=api_headers)
            print(response.status_code)
            # if response.status_code in [204, 200]:
            #     print("Employee added successfully in DB!")
            #     print(response.text)
            # else:
            response.raise_for_status()
            print("Employee added to DB")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
    
    def update_employee(self, id, employee):
        try:
            url = f'{self.base_url}/{str(id)}'
            api_headers = {
                'content-Type': 'application/json',
                'accept': 'application/json'
            }
            response = requests.put(
                url, data=json.dumps(employee), headers=api_headers)
            print(response.status_code)
            if response.status_code in [204, 200]:
                print("Employee updated successfully in DB!")
                print(response.text)
            else:
                print("failed to update Employee details in DB")
                print(response.text)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')


if __name__ == "__main__":
    src = SampleRestClient()

    # src.get_all_employees()
    # src.get_employee_by_id(1)
    # src.search_employee("avinash", 'jack@gmail.com')
    # src.update_employee(1, {
    #     'id': 5,
    #     'name': 'qwe',
    #     'email_id': 'qwe@ejd.com',
    #     'phone_number': "3445645"
    # })

    # src.delete_employee_by_id(1)
