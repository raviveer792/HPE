import json

#print(json.dumps("FOO")[0])
print(json.dumps("Foo")[3])

print(len(json.dumps(None)))

print(type(json.dumps("1.57")))

'''
def join_two_arrays(array_of_one,array_of_second):
    list_one=json.loads(array_of_one)
    list_two=json.loads(array_of_second)
    joined_list=list_one+list_two
    return json.dumps(joined_list)
print(join_two_arrays('["23","786"]','["13","78"]'))'''

array_of_one='["one","two"]'
array_of_two='["three","four"]'
#print(join_two_arrays(array_of_one,array_of_two))


def join_two_arrays(array_of_one, array_of_two):
    list_one = json.loads(array_of_one)
    list_two = json.loads(array_of_two)
    joined_list = list_one + list_two
    return json.dumps(joined_list)
print(join_two_arrays(array_of_one,array_of_two))





