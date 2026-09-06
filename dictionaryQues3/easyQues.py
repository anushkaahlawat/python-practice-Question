# 1.Create a dictionary and print it.
# 2.Access the value of a specific key.
# 3.Add a new key-value pair.
# 4.Update the value of an existing key.


'''print_right = {
    "name" : "anushka ahlawat",
    "age"  : 18,
    "favColor" : ["pink","white","yellow","maroon","black","offwhite"]
}


print(print_right)
print(print_right.get("name"))
print(print_right["age"])


print_right.update({"city" : "meerut"})
print(print_right.get("city"))


print_right.update({"favColor" : ["pink","yellow","red","blue","black","white"]}) 
print(list(print_right.get("favColor")))'''




#--------------------------------------------------------------------------------------------------------------


# 5.Delete a key from a dictionary.
# 6.Find the length of a dictionary.
# 7.Print all keys.


"""student = {
    "name" : "anushka ahlawat",
    "age"  : 18,
    "marks" : {"phy" : 80,"chem" : 79, "maths" : 69,"english" : 90,"phyEdu" : 95},
    "isPass" : "yes",
    "contactNo." : 7830709657,
    "grade"  : "A"  ,
    "more"  : "none"
}

print(student)

student["name"] = "Anushka Ahlawat"
print(student["name"])
print(len(student))

student.pop("more")
print(student)

print(student.keys())"""


#-----------------------------------------------------------------------------------------------------------

# 8.Print all values.
# 9.Print all key-value pairs.



'''stud = {
    "name" : "anushka ahlawat",
    "age"  : 18,
    "marks" : {"phy" : 80,"chem" : 79, "maths" : 69,"english" : 90,"phyEdu" : 95},
    "isPass" : "yes",
    "grade"  : "A"  
}


print(list(stud.values()))
print(list(stud.items()))
'''


#-----------------------------------------------------------------------------------------------------



# 10.Check whether a key exists in the dictionary.



info = {
    "name" : "grace",
    "age"  : 18,
    "contact" : 7830709657,
    "nature" : "amazing",
    "isBeautiful" : "very much"
}

if "name" in info :
    print("key exist in dictionary")
else:
    print("key is not exist in dictionary")

