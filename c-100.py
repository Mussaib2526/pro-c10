Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome to State bank of India")
Welcome to State bank of India
>>> p=int(input("Enter your 4 digit pin number: "))
Enter your 4 digit pin number: m = 25000
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    p=int(input("Enter your 4 digit pin number: "))
ValueError: invalid literal for int() with base 10: 'm = 25000'
>>> m = 25000
>>> if(p == 1234):
... print("1-Withdraw")
... print("2-Balance Enquiry")
... print("3-Fast Cash")
SyntaxError: expected an indented block after 'if' statement on line 1
>>> if(p == 1234):
... print("1-Withdraw")
... print("2-Balance Enquiry")
... print("3-Fast Cash")
... c = int(input("Please choose transactions: "))
SyntaxError: expected an indented block after 'if' statement on line 1
>>> if(p == 1234):
... print("1-Withdraw")
... print("2-Balance Enquiry")
... print("3-Fast Cash")
SyntaxError: expected an indented block after 'if' statement on line 1
>>> c = int(input("Please choose transactions: "))
... if (c == 1):
... w=int(input("Enter withdraw amount: "))
... if (w < m and w%100 == 0):
... print("Please take your amount:", w)
... else:
... print("Invalid cash")
SyntaxError: multiple statements found while compiling a single statement
>>> if(p == 1234):
... print("1-Withdraw")
... print("2-Balance Enquiry")
... print("3-Fast Cash")
c = int(input("Please choose transactions: "))
if (c == 1):
w=int(input("Enter withdraw amount: "))
if (w < m and w%100 == 0):
print("Please take your amount:", w)
else:
print("Invalid cash")
SyntaxError: expected an indented block after 'if' statement on line 1
m = 25000
if(p == 1234):
print("1-Withdraw")
print("2-Balance Enquiry")
print("3-Fast Cash")
SyntaxError: multiple statements found while compiling a single statement
print("Welcome to State bank of India")
p=int(input("Enter your 4 digit pin number: "))
m = 25000
if(p == 1234):
print("1-Withdraw")
print("2-Balance Enquiry")
print("3-Fast Cash")
c = int(input("Please choose transactions: "))
if (c == 1):
w=int(input("Enter withdraw amount: "))
if (w < m and w%100 == 0):
print("Please take your amount:", w)
else:
print("Invalid cash")

elif(c==2):
print("Your available amount : ",m)

elif (c == 3):
print("1->5,000")
print("2->10,000")
print("3->15,000")
print("4->20,000")
f = int(input("Enter fast cash option: "))
if (f == 1 and 5000 < m):
print("please take cash 5000")
elif (f == 2 and 10000 < m):
print("please take cash 10000")
elif (f == 3 and 15000 < m):
print("please take cash 15000")
elif (f == 4 and 20000 < m):
print("please take cash 20000")
else:
print("Invalid fast cash option")
else:
print("Wrong choice")
else:
print("Wrong pin number")
SyntaxError: multiple statements found while compiling a single statement

