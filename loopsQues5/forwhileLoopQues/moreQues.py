# 1.Check whether a number is an Armstrong number.



'''n = int(input("Enter a number: "))

original = n
total = 0

while n > 0:
    digit = n % 10
    total += digit ** 3
    n = n // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")'''



# 2.Check whether a number is a prime number using a while loop.



'''n = int(input("Enter a number: "))

i = 2
is_prime = True

if n < 2:
    is_prime = False

while i < n:
    if n % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")'''


    
# 3.Print all prime numbers from 1 to N.



'''N = int(input("Enter N: "))

n = 2

while n <= N:

    i = 2
    is_prime = True

    while i < n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(n)

    n += 1'''



    
# 4.Find the GCD/HCF of two numbers using a while loop.



'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

i = 1
gcd = 1

while i <= min(a, b):
    if a % i == 0 and b % i == 0:
        gcd = i
    i += 1

print("GCD is:", gcd)'''



# 5.Keep taking numbers from the user until they enter 0, then print the total sum.



'''total = 0

while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    total += n

print("Total sum:", total)'''



# 6.Keep taking numbers until the user enters a negative number, then print how many positive numbers were entered.



'''count = 0

while True:
    n = int(input("Enter a number: "))

    if n < 0:
        break

    if n > 0:
        count += 1

print("Positive numbers entered:", count)'''



# 7.Find the second largest digit in a number.



'''n = input("Enter a number: ")

largest = -1
second = -1

for i in n:
    digit = int(i)

    if digit > largest:
        second = largest
        largest = digit

    elif digit > second and digit < largest:
        second = digit

print("Second largest digit:", second)
'''



# 8.Check whether a number is a perfect number.



'''n = int(input("Enter a number: "))

total = 0
i = 1

while i < n:
    if n % i == 0:
        total += i
    i += 1

if total == n:
    print("Perfect number")
else:
    print("Not a perfect number")'''




# 9.Print the Fibonacci series up to N terms using a while loop.



'''n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")

    c = a + b
    a = b
    b = c

    i += 1'''




# 10.Create a simple menu-driven program using a while loop that keeps running until the user chooses "Exit".




'''while True:

    print("\n1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Sum:", a + b)

    elif choice == "2":

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Difference:", a - b)

    elif choice == "3":

        print("Exiting...")
        break

    else:
        print("Invalid choice")'''