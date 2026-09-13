# 1.Find the factorial of a number using a for loop.



'''n = int(input("enter a number :"))
fact = 1

for i in range(1,n+1):
    fact = fact*i
print(fact)'''
    
   

# 2.Count the number of digits in a number.



'''n = int(input("enter a number :"))
count = 0

for i in str(n):
    count += 1
print(count)'''



# 3.Find the sum of digits of a number.



'''n = input("enter a number :")
total = 0

for i in n:
    total += int(i)

print("the total sum of digits is",total)'''



# 4.Find the product of digits of a number.



'''n = input("enter a number :")
total = 1

for i in n:
    total *= int(i)

print("the product of the digits is",total)'''



# 5.Reverse a number using a for loop.



'''n = input("enter a number :")
rev = ""

for i in n:
    rev = i + rev

print("the reverse of a number ",rev)''' 



# 6.Check whether a number is a palindrome.




'''n = input("enter a number :")
rev = ""

for i in n:
    rev = i + rev

if n == rev:
    print("the number is palindrome ")
else:
    print("the number is not palindrome")'''



# 7.Count the number of even and odd digits in a number.



'''n = input("enter a number :")
even = 0
odd = 0

for i in n:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print("even numbers are",even)
print("odd numbers are",odd)'''



# 8.Find the largest digit in a number.



'''n = input("enter a number :")
large = 0


for i in n:
    if int(i) > large:
        large = int(i)
print("the largest number is",large)'''



# 9.Find the smallest digit in a number.



'''n = input("enter a number :")
smaller = 0

for i in n:
    if int(i) < smaller:
        smaller < int(n)
print("the smallest number is",smaller)'''



# 10.Count how many times a particular digit occurs in a number.



n = input("enter a number :")
target = input("enter the digit to count :")

count = 0


for i in n:
    if i == target:
        count += 1

print("the digit occurs",count,"times")