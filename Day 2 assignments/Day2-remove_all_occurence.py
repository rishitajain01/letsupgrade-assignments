#Assignment 2
#Q1)Delete all occurrences of an element in a list
list=[int(i) for i in input("Enter the list elements").split()]
x=int(input("enter the element to be removed"))
for i in list:
  if i==x:
    list.remove(i)
print(list)