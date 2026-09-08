# 1.Find the factorial of a number using a while loop.


'''n = int(input("Enter the number : "))
                                                    
i = 1
fact = 1
while i <= n:
    fact = fact*i
    i += 1
print("the factorial is ",fact)'''



#---------------------------------------------------------------------------------------------------------------


# 2.Count the number of digits in a number.


'''
num = int(input("enter the number : "))

count = 0
while num > 0:
    num = num // 10
    count += 1

print("the number of digits is",count)'''


#-----------------------------------------------------------------------------------------------------------------


# 3.Find the sum of digits of a number.



'''num = int(input("enter the numbers :"))

sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("the sum is", sum)'''



#-------------------------------------------------------------------------------------------------------------------


# 4.Find the product of digits of a number.



'''num = int (input("enter the number :"))

prod = 1
while num > 0:
    digit = num % 10
    prod *= digit
    num = num // 10

print("the product is",prod)'''



#----------------------------------------------------------------------------------------------------------------------


# 5.Reverse a number using a while loop.



'''num = int(input("Enter the number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("The reverse is:", reverse)'''



#----------------------------------------------------------------------------------------------------------------------


# 6.Check whether a number is a palindrome.



"""num = int(input("Enter the number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 1012345

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")"""



#-------------------------------------------------------------------------------------------------------------------


# 7.Count how many even and odd digits are present in a number.



'''num = int(input("Enter the number: "))

even = 0
odd = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    num = num // 10

print("Even digits:", even)
print("Odd digits:", odd)'''



#--------------------------------------------------------------------------------------------------------------


# 8.Find the largest digit in a number.



'''num = int(input("Enter the number: "))

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print("Largest digit:", largest)'''



#-------------------------------------------------------------------------------------------------------------


# 9.Find the smallest digit in a number.



'''num = int(input("Enter the number: "))

smallest = num % 10

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Smallest digit:", smallest)'''



#--------------------------------------------------------------------------------------------------------------


# 10.Count how many times a particular digit occurs in a number.



num = int(input("Enter the number: "))
target = int(input("Enter the digit to find: "))

count = 0

while num > 0:
    digit = num % 10

    if digit == target:
        count += 1

    num = num // 10

print("The digit occurs", count, "times")



#--------------------------------------------------------------------------------------------------------------


# 11.square of a number.


'''n = int(input("Enter the number : "))
                    
i = 1
while i <= n:
    print(n**i)
    i += 1'''