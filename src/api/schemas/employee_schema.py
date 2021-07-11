employee_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'email_id': {'type': 'string'},
        'phone_number': {'type': 'string'}
    },
    "required": [],
    "additionalProperties": False
}