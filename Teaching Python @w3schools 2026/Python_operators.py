#will learn about the operators in Python

#Arithmetic Operations
#These operators are used for methametical purposes and are used with  numeric values.
"""
| Operator | Description |
| --- | --- |
| + | Addition | To perfom addition, will give the sum of two or more numbers |
| - | Subtraction | To perform subtraction, will give the difference of two or more numbers |
| * | Multiplication | To perform multiplication, will give the product of two or more numbers |
| / | Division | To perfom division, will give the quotient of two or more numbers |
| % | Modulus | To perform modulus, will give the remainder of two or more numbers |
| ** | Exponentiation |  To perform exponentiation, will give the result of two or more numbers |
| // | Floor division | To perform floor division, will give the result of two or more numbers |
"""


#Addition operator
print(2 + 3) #Output 5
print(2 + 3 + 4) #Output 9
x = 90
y = 10
print(x + y) #Output 100

k = '10'
l = '20'  # noqa: E741
print(k + l) #Output 1020 --> Concatenation of two strings , if you needto perform numeric calculation, you need to convert the string to integer using int() function
print(int(k) + int(l)) #Output 30 --> Addition of two numbers after converting the string to integer using int() function 

#you can also use addition  operator on a sliced string
my_cellphone_number ='0711234567'
x1 = my_cellphone_number[2:5] #Output 112
x2 = my_cellphone_number[5:8] #Output 123
print (x1 + x2) #Output 112123 in string format
print (int(x1) + int(x2)) #Output 457 in integer format


#Subtraction operator
#please  note that the subtraction operator cannot be used with strings.
print(10 - 5) #Output 5
print(10 - 5 - 2) #Output 3
x = 90
y = 10
print(x - y) #Output 80

#Multiplication operator
print(2 * 3) #Output 6
print(2 * 3 * 4) #Output 24
x = 90
y = 10
print(x * y) #Output 900

k = '10'
l = '20'  # noqa: E741
print(int(k) * int(l)) #Output 200 --> Multiplication of two numbers after converting the string to integer using int() function

#Division operator
print(10 / 5) #Output 2
print(10 / 5 / 2) #Output 1
x = 90
y = 10
print(x / y) #Output 9

k = '10'
l = '20'  # noqa: E741
print(int(k) / int(l)) #Output 5 --> Division of two numbers after converting the string to integer using int() function

#Modulus operator
x = 90
y = 10
print(x % y) #Output 0

k = '10'
l = '20'  # noqa: E741
print(int(k) % int(l)) #Output 0 --> Modulus of two numbers after converting the string to integer using int() function

#Exponentiation operator
x = 90
y = 10 
print(x ** 2) #Output 8100
print(y ** 2) #Output 100
k = '10'
l = '2'  # noqa: E741
print(int(k) ** int(l)) #Output 100 --> Exponentiation of two numbers after converting the string to integer using int() function


#Floor Division operator
x = 90
y = 10
print(x // y) #Output 9

k = '10'
l = '2'  # noqa: E741
print(int(k) // int(l)) #Output 5 --> Floor Division of two numbers after converting the string to integer using int() function

#Next will be the Assignment Operators

#Assignment operator is used to assign values to variables.
"""
| Operator | Description |
| --- | --- |
| = | Assignment | To assign a value to a variable |
| += | Addition assignment | To add a value to a variable |
| -= | Subtraction assignment | To subtract a value from a variable |
| *= | Multiplication assignment | To multiply a value to a variable |
| /= | Division assignment | To divide a value to a variable |
| %= | Modulus assignment | To perform modulus on a variable |
| **= | Exponentiation assignment | To perform exponentiation on a variable |
| //= | Floor division assignment | To perform floor division on a variable |
| &= | Bitwise AND assignment | To perform bitwise AND on a variable |
| ^= | Bitwise XOR assignment | To perform bitwise XOR on a variable |
| \|= | Bitwise OR assignment | To perform bitwise OR on a variable |
|<<= | Left shift assignment | To perform left shift on a variable |
|> | Right shift assignment | To perform right shift on a variable |
|:= | Walrus operator | To assign a value to a variable in a conditional expression |
| |= | Assignment in conditional expressions | To assign a value to a variable in a conditional expression |

    
"""

#Walrus operator
#This operator is used to assign a value to a variable  and return that value in a larger expression.

#Normal way
count = [1, 2, 3, 4, 5]
print(f"The list has {len(count)} elements.")

# Using Walrus operator 
if(n:= len(count)) > 2:
    print(f"\nThe list has {n} elements.\nWalrus operator")
    
name = 'Philasande'
if(n:= len(name)) > 2:
    print(f"\nThe name has {n} characters.\nWalrus operator")
    
#I will skip others , I will create a page for them separately

#Ternary Operator
#This operator allows  you to assign one value in a condition if is true and another value if is false.
num = 6
x = 'Weekend' if num > 5 else 'Weekday' #ternanry operator structure/syntax
print(f"\nThe day is {x}.\nTernary operator used")

#Example 2
year_born = 2023
curr = abs(year_born - 2026)
vote = "Eligible to vote" if (curr) >= 18 else "Not eligible to vote"
print(f"\n{curr} year olds are {vote}.\nTernary operator used in example 2")

#Example 3
pass_mark = 60
mark = 45
results = 'Pass' if mark >= pass_mark else 'Fail'
print(f"\n{mark}% is {results}, try next year.\nTernary operator used in example 3")


#Comparison Operators 
"""
Comparison operators are used to compare two or more values in a code or instruction. 
| Operator | Description |
| --- | --- |
| == | Equal to | e.g  x ==y
| != | Not equal to | e.g x != y
| > | Greater than | e.g x > y
| < | Less than | e.g x < y
| >= | Greater than or equal to | e.g x >= y
| <= | Less than or equal to |  e.g x <= y
"""

#Equal operator
x = 10
y = 10
print(x == y) #Output True

#Not equal operator
x = 10
y = 20
print(x != y) #Output True

#Greater than operator
x = 10
y = 20
print(x > y) #Output False

#Less than operator
x = 10
y = 20
print(x < y) #Output True

#Greater than or equal to operator
x = 10
y = 20
print(x >= y) #Output False

#Less than or equal to operator
x = 10
y = 20
print(x <= y) #Output True

#Logical Operators
"""
Logical operators are used to combine multiple conditions in a single expression. 
| Operator | Description |
| --- | --- |
| and | Returns True if both conditions are True |
| or | Returns True if at least one of the conditions is True |
| not | Returns the opposite of the condition |
"""

#and operator
x = 10
y = 20
print(x > 5 and y < 10) #Output False

#or operator
x = 10
y = 20
print(x > 5 or y < 10) #Output True

#not operator
x = 10
y = 20
print(not x > 5) #Output False
print(not y < 10) #Output True

#Identity Operators
"""
Identity operators are used to compare two or more values in a code or instruction. 
| Operator | Description |
| --- | --- |
| is | Returns True if both values are the same |
| is not | Returns True if both values are not the same |
"""

#is operator
x = 10
y = 10
print(x is y) #Output True

#is not operator
x = 10
y = 20
print(x is not y) #Output True
print(y is not y) #Output False

#Membership Operators
"""
Membership operators are used to check if a value is present in a sequence or collection. 
| Operator | Description |
| --- | --- |
| in | Returns True if the value is present in the sequence or collection | 
| not in | Returns True if the value is not present in the sequence or collection |
"""
numbers = [1, 2, 3, 4, 5]
print(2 in numbers) #Output True
print(6 in numbers) #Output False

#not in operator
numbers = [1, 2, 3, 4, 5]
print(2 not in numbers) #Output False
print(6 not in numbers) #Output True

#Bitwise Operators
"""
Bitwise operators are used to perform operations on binary data. 
| Operator | Description |
| --- | --- |
| & | Bitwise AND | Returns the bitwise AND of two values |
| \| | Bitwise OR | Returns the bitwise OR of two values |      
| ^ | Bitwise XOR | Returns the bitwise XOR of two values |
| ~ | Bitwise NOT | Returns the bitwise NOT of a value |
| << | Left shift | Returns the left shift of a value |
| >> | Right shift | Returns the right shift of a value |
"""

#I will deal with them in the next module where we will be writing instructions to reveal the binary number of any decimal number system


