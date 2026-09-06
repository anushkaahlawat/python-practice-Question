# 1.Find the union without using union().


s1 = {1, 2, 3}
s2 = {3, 4, 5}

result = set(s1)
for i in s2:
    result.add(i)

print(result)



#---------------------------------------------------------------------------------------------------------



# 2.Find the intersection without using intersection().



s3 = {1, 2, 3, 4}
s4 = {3, 4, 5, 6}

result = set()

for i in s3:
    if i in s4:
        result.add(i)

print(result)


#---------------------------------------------------------------------------------------------------------------



# 3.Find the difference without using difference().
# 4.Remove duplicate words from a sentence using a set.
# 5.Count the number of unique vowels in a string.
# 6.Check whether two sets are equal.
# 7.Create a set of squares from 1 to 10.
# 8.Find the sum of all elements in a set.
# 9.Print only even numbers from a set.
# 10.Print only odd numbers from a set.