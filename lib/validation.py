import jsonschema
from jsonschema import validate


def jsonvalidator(schema: dict, json: dict):
    try:
        validate(instance=json, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
