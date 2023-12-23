"""
conditional structures: mechanism to branch out in the code
condition must either true of false
len(str) == 5
if 
else

1. Check Even Odd 
2. Check if year is leap 
3. Check Positive, Negative, or Zero
4. Compare Two Numbers
5. Determine the Largest among Three Numbers
6. Check Alphabet
7. Check Vowel or Consonant
8. Determine Quadrant of a Coordinate
9. Check Valid Triangle
10. Check for Palindrome Number
"""
# print(False&False|False)
# print(len("str") == 5&len("something else must be 10")>=10|len("something else must be 5")>=5)
# print(False&(True|True))

print("Start of the if program")
if True:
    print("First If is true")
print("End of of first if")
if False:
    print("Second IF is true")
else:
    print("Second IF is false so running else")
print("End of of second if")
if False:
    print("Third IF was false but now is true")
print("End of of fourth if")
if True:
    print("Fourth IF is True")
print("End of of fourth if")