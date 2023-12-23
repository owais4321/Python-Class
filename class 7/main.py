"""
a = [1,2,3,4] C struct
b = a b is the reference to a

key value pair

{key:value,
key:value}
"""
# a = "owais"
# b = a
# b = "A"
# print(a,b)


# a = [1,2,3,4]
# b = a
# a[0] = 3
# b[1] = 5
# print(a)  #[1,2,3,4]
# print(b)  # [1,5,3,4]
#copy

student = {
    'name':'Alan Turing',
    'batch':'18',
    'dept':'Mathematics',
    'age' : 45,
    'dept_choices':['SWE','DS','AI'],
    'address':{
        'street':'Street NO XYZ',
        'House':'House No 009',
        'Country':'Pakistan',
        'Postal Code':9001
    }
}
student['address']['Postal Code']
student['dept_choices'][2]
print(student.pop('age'))
student['id'] = '18MT89'
student['dept'] = 'AI'
print(student)
del student['dept']
print(student)
# students = [
#     {
#     'name':'Alan Turing',
#     'batch':'18',
#     'dept':'Mathematics'
# },

# {
#     'name':'Alan Turing',
#     'batch':'18',
#     'dept':'Mathematics'
# }
# ]
# name = ["Alan Turning"]
# batch = ["18"]
# dept = ["Mathematics"]