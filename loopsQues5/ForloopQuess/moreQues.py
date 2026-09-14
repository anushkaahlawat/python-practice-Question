# 1.Print each character of a string on a new line.



'''n = input("enter a string :")

for i in n:
    print(i)'''



# 2.Count the number of vowels in a string.




'''n = input("enter a string : ")
count = 0

for i in n:
    if i in "aeiou":
        count += 1    
print("number of vowel in a string is",count)
'''



# 3.Count the number of consonants in a string.



'''n = input("enter a string :")
count = 0 

for i in n:
    if i not in "aeiou":
        count += 1
print("the number of consonants in a string is",count)'''



# 4.Count the number of spaces in a sentence.



'''text = input("enter a string :")
count = 0

for i in text:
    if i == " ":
        count += 1
print("the number of spaces is",count)'''


    
# 5.Count how many times a particular character appears in a string.



'''txt = input("enter a string : ")
target = input("enter the targeted character : ")
count = 0

for i in txt:
    if i == target:
        count += 1
print("the repeated character is appears",count,"times")'''



# 6.Print only the even-position characters of a string.




'''n = input("enter a string : ")

for i in range(len(n)):
    if i % 2 == 0:       
        print("even position characters is",n[i])'''



# 7.Print a string in reverse order using a for loop.



'''n = input("enter a string : ")
rev = ""

for i in n:
    rev = i + rev
print("string in reverse order",rev)'''



# 8.Find the largest digit present in a string containing numbers.



'''n = input("enter a number :")
count = 0

for i in n:
    if int(i) > count:
        count = int(i)
print("the largest number is",count)'''



# 9.Check whether a number is prime using a for loop.



'''n = int(input("enter a number : "))
is_prime = True
if n < 2:
    is_prime = False

for i in range(2,n):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
        print("the number is prime")
else: 
        print("the number is not prime")'''



# 10.Print all prime numbers from 1 to N.



N = int(input("Enter N: "))

for n in range(2, N + 1):

    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n)
 