#Homework 1

#Create two lists. The first list should consist of odd numbers. The second list is also of even numbers.
#Merge these two lists. Multiply all values in the new list by 2.
#Use a loop to print the data type of the all values in the new list.

mylist1 = [1, 3, 5, 7, 9, 11]
mylist2 = [2, 4, 6, 8, 10, 12]

mylist1.extend(mylist2)

mylist3 = [i * 2 for i in mylist1]

for i in mylist3:
    type(i)



