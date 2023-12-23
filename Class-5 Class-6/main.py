strHtml = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello world</h1>
    <p>This is paragraph</p>
</body>
</html>
"""
# name1 = "Dr. Owais"
# name2 = "Prof. John Doe"
# name3 = "Prof Dr. Jane Doe"

# title3 = name3.split(".")
# print(title3[0])
# openHTMLTAG = strHtml.index("<p>")
# print(openHTMLTAG)
# closeHTMLTAG = strHtml.index("</p>")
# print(closeHTMLTAG)
# print(strHtml[217:234])

lst = ["Zoha","Ali","Adil","Roma",1,2,3,3.4,3+2j,90,[12,2,3],[5,4,3,[12,3,4,9]]]
print(lst)
lst2 = [1,2,3,4,5] # => 1 -> 0 .... 5 -> 4
# accessing single element
print(lst2[-3])

#nested list value extraction
print(lst[11][3][1:3])

# accessing multiple elements sub-list
print(lst2[2:3])

#length of list
print(len(lst))

# adding elements to list
lst.append(3)
print(lst)
#inset, Extend
lst.remove(3)
print(lst)
print(lst.pop(3))
print(lst)
del lst[2]
print(lst)