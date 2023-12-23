"""
two types of function, one returns something other don't

return they may or may not effect the variable on which 
these functions are being used

In Set A-B != B-A
A-B means elements in A which are not in B
B-A means elements in B which are not in A

a = 2 = assignment operator
+=,-=,*=,/=,//=,%=**=

comparison operator
==,!=,<,>,<=,>=
"""
# a = [1,2,3,4,5,6]
# print(a.remove(1))
# print(a)

# a = [1,2,3,4,5,6]
# print(a.pop(1))
# print(a)

# a = "THIS is New"
# print(a.lower())
# print(a)


# N = {1,2,3,4,5}
# W = {0,1,2,3,4}
# Z = {-3,-2,-1,0,1,2,3}
#W-N
#Z-W = {-3,-2,-1} 
#Z-N = {-3,-2,-1,0}
# print(Z) #Z = {-3,-2,-1,0,1,2,3}
# print(Z.difference_update(W))  #None #{-3,-2,-1}
# print(Z) #{-3,-2,-1}

a = 2
# a = a*10  #a = 20
# a = a*4   #a = 80
print(a) #2
a+=2
print(a) #2+2
a*=2
con = 2>3
print(con)