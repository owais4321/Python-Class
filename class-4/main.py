"""
Home Work Related
Positive
Hello world 0->H 1->e 2->l 3->                           ---------->
Negative Indexs Hello world -1->d -2->l -3->r -4->o      <---------
[start:end+1]

Class work
Changing case of a string
Hello world => hello world HELLO WORLD
lower
upper
title
capital 
swapcase

count 

"""

str1 = "HEllo wOrld" #---->
# lower_str = str1.lower()
# str1 = str1.lower()
# print(str1[-3])
print(str1,str1.lower())
print(str1,str1.upper())
print(str1,str1.title())
print(str1,str1.capitalize())
print(str1,str1.swapcase())
print(str1,str1.count("O"))
print(str1,str1.count("h"))
print(str1.lower(),str1.lower().count("o"))
document = " Hey, Buddy what's up, all good. Weather is amazing "
new_sentences = document.split(".")
print(new_sentences)
new_sentence = document.replace("Buddy","Friend")
print(new_sentence.strip().split())

