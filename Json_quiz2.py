import json


def jsonize_if_not_already(value):
    try:
        value = json.loads(value)
    except ValueError:
        pass
    return json.dumps(value)

print(jsonize_if_not_already("ONE"))
print(jsonize_if_not_already('"ONE"'))
#print(jsonize_if_not_already(False))    TypeError: the JSON object must be str, bytes or bytearray, not 'Boolean'
print(jsonize_if_not_already("false"))
print(jsonize_if_not_already("1"))
#print(jsonize_if_not_already(1))    TypeError: the JSON object must be str, bytes or bytearray, not 'int'


