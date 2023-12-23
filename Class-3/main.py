"""
String is basically sequence of characters enclosed in 
String is used reprents text "1234" "owais*-)_" ""

+ - * / // %

+ string to string Cantentation

- None

* Between Number and String

/ None

// None

%  None

Slicing a string
str[index]
roll_number = 15SW50 Batch, Dept, ID_NUMBER
str[start:end+1]  
str[0:1+1] = str[0:2]
str[2:4] 
"""
# str1 = "Hello World"
# str2 = str1 + "1"
# # print(str2)
# str3 = str2*2
# # print(str3)
# print("*"*1)
# print("*"*2)
# print("*"*3)
# print("*"*4)
# print("*"*5)
str1 = "15SW1"  #0->1 1->5 2->S....
# print(str1[4])
batch = str1[0:2]
print("Batch",batch)
dept = str1[2:4]
print("Department",dept)
number = str1[4:]
print("Number is",number)