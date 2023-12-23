"""
Given an "out" string length 4, such as "<<>>", and a word, 
return a new string where the word is in the middle of the out string, e.g. "<<word>>".
make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'

3 operator
Arthemtic
Assignment /Compound assignment
comparison operator

Logical Operators

And Or Not
AND: All True then else false
OR: Atleast one true 
NOT: Makes true False and False True
if else 

Conditional Structures
"""
# out = "[[]]"
# word = "word"
# print(out[:2]+word+out[2:])
# cond1 = False
# cond2 = True
# cond3 = False
# print(not cond2)

# a = 2
# b = 3
# odd = b%2!=0  #false   
# even = not odd #true
# print(odd)

# if (True):
#     excute this
#     this
#     and this
# otherwise:
#     excute that
#     that
#     and that

if (not 1==1 or not not not 1!=1):
    print("IF")
# print("Back to linear execution")
if (True):
    print("IF-2")
if (True):
    print("IF-3")
else:
    print("Else")