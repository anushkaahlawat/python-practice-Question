# 1.Concatenate two tuples.


#tup1 = (10,20,30,40,50)
#tup2 = (60,70,80,90,100)


#tup3 = tup1 + tup2
#print("after concatenation :", tup3)


#-------------------------------------------------------------------------------------------------

# 2.Repeat a tuple using the * operator.



#tupp = (10,20,30,40,50)
#print(tupp*5)



#--------------------------------------------------------------------------------------------------


# 3.Convert a tuple into a list.



#tut =  ("brush","lipstick","lipgloss","lipbalm","liptint","lipblush")
#list1 = list(tut)
#print(list1)


#------------------------------------------------------------------------------------------------------


# 4.Convert a list into a tuple.
# 5.Reverse a tuple.



#li = ["pink","yellow","black","blue","maroon","green","beign"]
#print(li[::-1])


#tuple1 = tuple(li)
#print(tuple1)



#------------------------------------------------------------------------------------------------------


# 6.Print all tuple elements using a for loop.

#t = (3,2,4,5,6,6,8,9,9,5)

#for i in t:
   # print(i)


#--------------------------------------------------------------------------------------------------------


# 7.Count even and odd numbers in a tuple.



#tic= (10, 15, 20, 25, 30)

#even = 0
#odd = 0

#for i in tic:
 #   if i % 2 == 0:
   #     even += 1
   # else:
   #     odd += 1

#print("Even:", even)
#print("Odd:", odd)

   
        
#--------------------------------------------------------------------------------------------------------



# 8.Find the second largest element.
# 9.Find the second smallest element.


#t = (20,30,10,5,8,40,50,17)

#list1 = list(t)
#list1.sort()

#print("the largest element is :",list1[-2])
#print("thr smallest element is :",list1[1])



#-----------------------------------------------------------------------------------------------------------


# 10.Sort a tuple in ascending order.

#tpp = (1,2,3,45,6,7,8,9,9,10)
#list2 = sorted(tpp)
#print("after sorting :",tuple(list2))



#-------------------------------------------------------------------------------------------------------------



# 11.Remove duplicate elements from a tuple (by converting it to a set or list).


#t = (10, 20, 20, 30, 40, 40, 50)
#t1 = tuple(set(t))

#print("Tuple after removing duplicates:", t1)


#------------------------------------------------------------------------------------------------------------------



# 12.Slice a tuple to print specific elements.


#t = (10, 20, 30, 40, 50, 60)

#print("First three elements:", t[:3])
#print("Last three elements:", t[3:])
#print("Middle elements:", t[2:5])



#----------------------------------------------------------------------------------------------------------------




# 13.Find the product of all tuple elements.


#t = (2, 3, 4, 5)
#product = 1

#for i in t:
#    product = product * i

#print("Product =", product)


#---------------------------------------------------------------------------------------------------------



# 14.Merge two tuples.


#tuple1 = ("apple","banana","mango")
#tuple2 = ("litchi","watermelon","blueberry","papaya")

#tuple3 = tuple1 + tuple2

#print("After adding both tuples :",tuple3)


#----------------------------------------------------------------------------------------------


# 15.Find the maximum and minimum without using max() or min().



tic = (40, 10, 80, 20, 50)

largest = tic[0]
smallest = tic[0]

for i in tic:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)