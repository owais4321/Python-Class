"""
letter = 'A'
print(letter.lower())
print(2+3>4)
if(2+3>4):
print("Yes")
a + b > c
# a + c > b
# c + b > a
a = 10001
rev = 10001

# if False:
#     print("IF")
# elif True:
#     print("Else if")
# if True:
#     print("If 2")
# else:
#     print("Else") 
grade = 80
if grade>=80:
    print("A+")
elif grade>70:
    print("A")
elif grade>60:
    print("B")
else:
    print("C")
"""
import random
# Street Fighter 
p1 = "Player 1"
p2 = "Player 2"
p1_powers = ["punch", "kick","Haduken","upper kick","block"]
p2_powers = ["punch", "kick","Slam Buster","upper kick","block"]
p1_life = 100
p2_life = 100
while p1_life>=0 or p2_life>=0:
    power = int(input("Select your power"))
    if(power == 0):
        print("player 1 life is ",p1_life)
        print("Player 1 just hit",p1_powers[power])
        p2_life-=5
    elif power == 1:
        print("player 1 life is ",p1_life)
        print("Player 1 just hit",p1_powers[power])
        p2_life-=5
    elif power == 2:
        print("player 1 life is ",p1_life)
        print("Player 1 just hit",p1_powers[power])
        p2_life-=15
    elif power == 3:
        print("player 1 life is ",p1_life)
        print("Player 1 just hit",p1_powers[power])
        p2_life-=10
    elif power == 4:
        print("player 1 life is ",p1_life)
        print("Player 1 just hit",p1_powers[power])
    power2 = random.randint(0,5)
    if(power2 == 0):
        print("player 2 life is ",p2_life)
        print("Player 2 just hit",p1_powers[power2])
        p1_life-=5
    elif power2 == 1:
        print("player 2 life is ",p2_life)
        print("Player 2 just hit",p1_powers[power2])
        p1_life-=5
    elif power2 == 2:
        print("player 2 life is ",p2_life)
        print("Player 2 just hit",p1_powers[power2])
        p1_life-=15
    elif power2 == 3:
        print("player 2 life is ",p2_life)
        print("Player 2 just hit",p1_powers[power2])
        p1_life-=10
    elif power2 == 4:
        print("player 2 life is ",p2_life)
        print("Player 2 just hit",p1_powers[power2])
        

if(p1_life<=0):
    print("Player 2 is winner")
elif(p2_life<=0):
    print("player 1 is winner")