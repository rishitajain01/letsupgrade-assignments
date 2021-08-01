#Assignment 1
#Take input for a list and sort it in descending order.
list=input("enter the integer values of list seperated by space")
list=[int(i) for i in list.split()]
list.sort()
list.reverse()
print(list)