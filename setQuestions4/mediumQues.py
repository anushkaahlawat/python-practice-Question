# 1.Find the union of two sets.



'''s1 = {1,2,3,4,5}
s2 = {6,4,3,2,1,7}

print(s1.union(s2))'''



# 2.Find the intersection of two sets.



'''set1 = {1,2,3,4,5}
set2 = {6,4,3,2,1,7}

print(set1.intersection(set2))'''



# 3.Find the difference between two sets.



'''s3 = {1,2,3,4,5}
s4 = {6,7,8,1,5,2}

print(s3.difference(s4))'''



# 4.Find the symmetric difference of two sets.



'''set3 = {1,2,3,4}
set4 = {5,6,7,8}

print(set3.symmetric_difference(set4))'''



# 5.Remove duplicate elements from a list using a set.



'''s ="apple banana apple mango mango"

words = s.split()
unique_words = set(words)
print(unique_words)'''



# 6.Check whether one set is a subset of another.



'''s1 = {1,2,3,4,5}
s2 = {1,2,5,6,7,3}

if s1.issubset(s2):
    print("s1 is the subset of s2")
else:
    print("s1 is not a subset of s2")'''



# 7.Check whether two sets are disjoint.



'''set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}

if set1.isdisjoint(set2):
    print("sets are disjoin ")
else:
    print("sets are not disjoined")'''



# 8.Find the common elements in two sets.



'''s3 = {1,2,3,4,5,6}
s4 = {1,4,5,6,7,8}

common_elem  = s3.intersection(s4)
print("the common elements are",common_elem)'''



#----------------------------------------------- or -------------------------------------------------------------------


'''s1 = {1,2,3,4}
s2 = {3,4,5,6}

for i in s1:
    if i in s2:
        print(i)'''



# 9.Count the number of elements in a set.


'''set = {1,2,3,4,5,6,7,8,9,10}

count = len(set)
print(count)'''


#-------------------------------------------------- or --------------------------------------------------


'''s = {1,2,3,4,5,6,7,8,9,10,11}
count = 0

for i in s:
    count += 1
print("Number of elements:", count)'''


# 10.Find all unique elements from two lists using sets.



l1 = [1,2,3,4,5,6,7]
l2 = [1,6,7,8,9,10,11]


s1 = set(l1)
s2 = set(l2)

unique = s1|s2

print("the unique elements are",unique)

