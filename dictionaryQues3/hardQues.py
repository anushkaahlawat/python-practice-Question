# 1.Sort a dictionary by values.



'''info = {
    "color" : "white",
    "AnotherColor" : "maroon",
    "name" : "srishti",
    "looks" : "cute",
    "nature" : "preety good"
}

sort_data = dict(sorted(info.items()))
print(sort_data)'''



#----------------------------------------------------------------------------------------------------------



# 2.Reverse the keys and values of a dictionary.



'''student = {
    "Anu": 80,
    "Riya": 95,
    "Neha": 90
}

new_dict = {}

for key,value in student.items():
    new_dict[value] = key
print(new_dict)'''



#-------------------------------------------------------------------------------------------------------------



# 3.Create a dictionary from two lists (keys and values).



"""info1 = ["name","age","city","favColor"]
info2 = ["Anushka",18,"Meerut","Maroon"]


student_info = dict(zip(info1, info2))
print(student_info)"""




#---------------------------------------------------------------------------------------------------------------



# 4.Find the sum of all dictionary values.



'''marks = {
    "Chem" : 87,
    "phy"  : 89,
    "maths" : 75,
    "english" : 92
}


marks_Sum = sum(marks.values())

print("sum of the values is",marks_Sum)'''



#----------------------------------------------------------------------------------------------------------



# 5.Find the average of all dictionary values.



'''mark = {
    "Chem" : 87,
    "phy"  : 89,
    "maths" : 75,
    "english" : 92
}

dict_avg = sum(mark.values()) / len(mark)
print("average of the dictionary is",dict_avg)'''



#----------------------------------------------------------------------------------------------------------------



# 6.Print only keys whose values are greater than 50.



"""marks_val = {
    "Chem" : 87,
    "phy"  : 89,
    "maths" : 75,
    "english" : 92,
    "phyEdu" : 49
}


for key, value in marks_val.items():
    if value > 50:
         print(key)"""




#-----------------------------------------------------------------------------------------------------



# 7.Create a nested dictionary and print it.



"""students = {
    "student1": {
        "name": "Anu",
        "age": 19
    },
    
    "student2": {
        "name": "Riya",
        "age": 20
    }
}

print(students)"""



#-------------------------------------------------------------------------------------------------------------



# 8.Access values from a nested dictionary.




"""students = {
    "student1": {
        "name": "Anu",
        "age": 19
    },
    
    "student2": {
        "name": "Riya",
        "age": 20
    }
}


print(students["student1"]["name"])
print(students["student2"]["age"])"""




#------------------------------------------------------------------------------------------------------



# 9.Find duplicate values in a dictionary.




'''student = {
    "Anu": 80,
    "Riya": 90,
    "Neha": 80,
    "Srishti": 70,
    "Pooja": 90
}

values = list(student.values())

for value in set(values):
    if values.count(value) > 1:
        print(value)
'''




#-----------------------------------------------------------------------------------------------------------




# 10.Count the number of vowels in a string using a dictionary.





text = "hello world"

vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

for ch in text:
    if ch in vowels:
        vowels[ch] += 1

print(vowels)