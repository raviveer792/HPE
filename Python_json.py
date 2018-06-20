'''import json

j_data='{"name":"Rahul","age":39,"available":true}'

jsonToPython=json.loads((j_data))
print(jsonToPython)
print(json.dumps(jsonToPython))'''


'''import json

json_data="""{
"integer": 1,
"inner_object":{
"Nothing":null,
"Boolean":false,
"string":"foo"},
"list_of_string":["one","Two"]

}"""
python_dict=json.loads(json_data)
print(python_dict)
'''
'''
import json
student='{"101":{"class":"v","Name":"Rohit","Roll_no":7},' \
         '"102":{"class":"v","Name":"David","Roll_no":8},'\
         '"103":{"class":"v","Name":"Soniya","Roll_no":9}}'

s_Data=json.loads(student)
print(s_Data)
print(json.dumps(s_Data))'''

import json

student='{"Enrolment":"101","batch":[{"name":"x","fee":20000},' \
        '{"name":"Rahul","fee":30000},' \
        '{"name":"YZ","fee":40000}]}'

s_Data=json.loads(student)
print(s_Data)
print(json.dumps(s_Data))