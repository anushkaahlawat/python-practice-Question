# 1.Find the union without using union().


'''s1 = {1, 2, 3}
s2 = {3, 4, 5}

result = set(s1)
for i in s2:
    result.add(i)

print(result)'''



#---------------------------------------------------------------------------------------------------------



# 2.Find the intersection without using intersection().



'''s3 = {1, 2, 3, 4}
s4 = {3, 4, 5, 6}

result = set()

for i in s3:
    if i in s4:
        result.add(i)

print(result)'''


#---------------------------------------------------------------------------------------------------------------



# 3.Find the difference without using difference().



'''s1 = {1,2,3,4,5,6}
s2 = {1,4,6,7,9,8}


result = s1 - s2
print("the difference is", result)'''



# 4.Remove duplicate words from a sentence using a set.



'''s = "apple banana mango orange apple orange mango grapes"

word = s.split()
uniq_word = set(word)

print(uniq_word)'''



# 5.Count the number of unique vowels in a string.



'''text = "hello world"

vowels = set()

for ch in text:
    if ch in "aeiou":
        vowels.add(ch)

print("Unique vowels:", vowels)
print("Number of unique vowels:", len(vowels))'''



# 6.Check whether two sets are equal.



'''s3 = {1,2,3,4,5,6}
s4 = {1,2,7,8,9}

check = s3 == s4
print(check)'''



#----------------------------------- or ------------------------------------------------------------



'''s3 = {1,2,3,4,5}
s4 = {1,2,3,4,5,6}

if s3 == s4:
    print("sets are equal")
else:
    print("sets are not equal")'''



# 7.Create a set of squares from 1 to 10.



'''sqr = set()

for i in range(1, 11):
    sqr.add(i * i)
print(sqr)'''



# 8.Find the sum of all elements in a set.



'''s = {1,2,3,4,5,6,7,8,9}

sum = 0
for i in s:
    sum += i
print("the sum of all elements is",sum)'''



# 9.Print only even numbers from a set.



'''s = {1,2,3,4,5,6,7,8,9}

for i in s :
    if i % 2 == 0:
        print("the even numbers are", i)'''



# 10.Print only odd numbers from a set.



set = {1,2,3,4,5,6,7,8,9,10}

for i in set:
    if i % 2 != 0:
      print("the odd numbers are", i)