# 1.Merge two dictionaries.



'''s1 = {
    "name" : "grace",
}


s2 = {
   "Name" : "anushka ahlawat",
}

s1.update(s2)
print(s1)'''



#-----------------------------------------------------------------------------------------------------------

# 2.Copy a dictionary.



"""dress = {
    "tshirt" : 500,
    "top"   : 600,
    "jeans" : 1000,
    "kurti" : 1200,
    "lehnga" : 50000
}

D = dress.copy()
print(D)
"""


#-----------------------------------------------------------------------------------------------------------



# 3.Clear all elements from a dictionary.



'''Drop = {
    "tshirt" : 500,
    "top"   : 600,
    "jeans" : 1000,
    "kurti" : 1200,
    "lehnga" : 50000
}

print(Drop)
print(Drop.clear())'''



#----------------------------------------------------------------------------------------------------------



# 4.Remove a key using pop().



'''student = {
    "name" : "anushka ahlawat",
    "age"  : 18,
    "marks" : {"phy" : 80,"chem" : 79, "maths" : 69,"english" : 90,"phyEdu" : 95},
    "isPass" : "yes",
    "grade"  : "A"  
}

print(student)
print(len(student))

student.pop("grade")
print(student)'''




#---------------------------------------------------------------------------------------------------------



# 5.Remove the last inserted item using popitem().


'''
s = {
    "name" : "anushka ahlawat",
    "age"  : 18,
    "marks" : {"phy" : 80,"chem" : 79, "maths" : 69,"english" : 90,"phyEdu" : 95},
    "isPass" : "yes",
    "grade"  : "A"  
}


s.popitem()
print(s)'''



#--------------------------------------------------------------------------------------------------------



# 6.Count the frequency of characters in a string.



"""text = "Anushka ahlawat"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)"""



#-----------------------------------------------------------------------------------------------------------



# 7.Count the frequency of words in a sentence.



'''word = "super cute, adorable and amazing"

freq = {}

for ch in word:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)'''



#------------------------------------------------------------------------------------------------------------



# 8.Find the key with the largest value.
# 9.Find the key with the smallest value.



"""dress = {
    "tshirt" : 500,
    "top"   : 600,
    "jeans" : 1000,
    "kurti" : 1200,
    "lehnga" : 70000,
    "onePiece" : 40000 
}


largest_keys = max(dress, key=dress.get)
smallest_keys = min(dress, key=dress.get)
sorted_keys = dict(sorted(dress.items()))


print("hightest price is of ",largest_keys)
print("smallest price is of",smallest_keys)
print(sorted_keys)"""



#-----------------------------------------------------------------------------------------------------



# 10.Sort a dictionary by keys.



std = {
    "Neha": 80,
    "Anu": 90,
    "Riya": 85
}

sorted_student = dict(sorted(std.items()))

print(sorted_student)