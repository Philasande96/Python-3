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
l = '20'
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
l = '20'
print(int(k) * int(l)) #Output 200 --> Multiplication of two numbers after converting the string to integer using int() function

#Division operator
print(10 / 5) #Output 2
print(10 / 5 / 2) #Output 1
x = 90
y = 10
print(x / y) #Output 9

k = '10'
l = '20'
print(int(k) / int(l)) #Output 5 --> Division of two numbers after converting the string to integer using int() function

#Modulus operator
x = 90
y = 10
print(x % y) #Output 0

k = '10'
l = '20'
print(int(k) % int(l)) #Output 0 --> Modulus of two numbers after converting the string to integer using int() function

#Exponentiation operator
x = 90
y = 10 
print(x ** 2) #Output 8100
print(y ** 2) #Output 100
k = '10'
l = '2'
print(int(k) ** int(l)) #Output 100 --> Exponentiation of two numbers after converting the string to integer using int() function


#Floor Division operator
x = 90
y = 10
print(x // y) #Output 9

k = '10'
l = '2'
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