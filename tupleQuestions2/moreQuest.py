# 1.Check if two tuples are equal.


#tup_1 = (2,4,6,8,10)
#tup_2 = (2,4,6,8,10)

#if tup_1 == tup_2:
  #  print("both are equal")
#else:
 #   print("both is not equal")



#-----------------------------------------------------------------------------------------------


# 2.Find the common elements in two tuples.


#tup1 = (2,4,6,8,10)
#tup2= (2,4,7,9,3)

#for i in tup1:
 #   if i in tup2:
  #      print("common element is :", i)



#------------------------------------------------------------------------------------------------



# 3.Count positive and negative numbers in a tuple.

#tt = (1,-2,-3,4,6,7,4,-9,-20,6)

#positive = 0
#negative = 0

#for i in tt:
#    if i >= 0:
#        positive += i
#    else:
#        if i <= 0:
#            negative += i

#print("the positive elements are :", positive)
#print("the negative elements are :", negative)



#-------------------------------------------------------------------------------------------------


# 4.Print elements at even indexes only.


t = (10,20,30,40,50)

even = 0
for i in t:
  if i % 2 == 0:
    even += i


print ("even number are ", even )
   



#-----------------------------------------------------------------------------------------------------



# 6.Find the frequency of every element in a tuple.


'''t = (10,20,30,40,40,40,10,10,10,50,60,60,50,40)

for i in set(t):
  print(i,"appears",t.count(i),"times")'''



#---------------------------------------------------------------------------------------------------



# 7.Create a nested tuple and print each element.


#t = ((10, 20), (30, 40), (50, 60))

#for i in t:
#    print(i)



#-------------------------------------------------------------------------------------------------



# 8.Swap the first and last elements of a tuple (by converting it to a list).


'''
t = (10, 20, 30, 40, 50)

list1 = list(t)

list1[0], list1[-1] = list1[-1], list1[0]
t = tuple(list1)
print(t)'''



#----------------------------------------------------------------------------------------------------


# 9.Find the sum of even numbers only.


#t = (10,15,20,25,30,35,40)
#sum_even = 0

#for i in t:
 #   if i % 2 == 0:
  #      sum_even += i

#print("Sum of Even Numbers =", sum_even)



#-----------------------------------------------------------------------------------------------------


# 10.Find the sum of odd numbers only.



#t = (10,15,20,25,30,35,40)
#sum_odd = 0

#for i in t:
#    if i % 2 != 0:
#       sum_odd += i

#print("the sum od odd numbers is :", sum_odd)
