# 1.Create a set and print its elements.
# 2. Add an element to a set.
# 3.Remove an element from a set.
# 4.Find the length of a set.



"""set = {10,20,30,40,50,60,70}

print(set)
print(len(set))
print(type(set))


set.add(80)
set.add(90)
print(set)

set.remove(70)
print(set)"""




#-----------------------------------------------------------------------------------------------------




# 5.Check whether an element exists in a set.



"""coll = {13,2,5,"anu",6,10,55}

if "anu" in coll:
    print("element is exist in set")
else:
    print("element is not exist in list")"""




#-------------------------------------------------------------------------------------------------------



# 6.Print all elements using a loop.


'''elem = {10,20,30,40}

for i in elem:
    print(elem)'''


#--------------------------------------------------------------------------------------------------------


# 7.Copy a set.


'''s = {2,3,4,5,6}


s1 = s.copy()
print(s1)'''



#-----------------------------------------------------------------------------------------------------------



# 8.Clear all elements from a set.



'''st = {"anushka",20,34,46}


st.clear()
print(st)
'''


#------------------------------------------------------------------------------------------------------------



# 9.Find the largest element in a set.
# 10.Find the smallest element in a set.


s = {10, 20, 30, 40}

print("the maximum element in the set is",max(s))
print("the minimum element in the set is",min(s))