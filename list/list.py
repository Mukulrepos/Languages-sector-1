# tuple use it the () this brackets is called a tuple
# it can not be change 

a =[1,2,3,4,5]#it is a list
b =(1,2,3,4,5)# it is a tuple
c ={1,2,3,4,5}#it is a set
d =[6,7,8,9,10]
print(type(a))
print(type(b))
print(type(c))

# frist is a list

# access by the index number
print(a[2:])# starting number is index number after this : use this to access all the elements in the list or a tuple or a set or a dictionary


#check the elements is are under or not 
if 2 in a:
    print("yes 2 is exist in the list ")
else:
    print("NO")
    
#  change the item is using the index in the list
a[2]="hello"
print(a)

#change the elements using the index group 
a[1:3]=["budy","brother"]
print(a)


# insert the elents in the list 
a.insert(1,"Vahanam")
print(a)

#  append use to allow the elements can access in the end of the list 
a.append("34532")
print(a)


# extend use to join the second list at the end of the frist list
a.extend(d)
print(a)

#  remove specific item in the list
a.remove("budy")
print(a)

# remove at the end of the list
a.pop()
print(a)

#  remove the item using the del function
del a[1]
print(a)

# delete list in the localhost
# del a
# print(a)

# clear all the list items
# a.clear()
# print(a)

# walktrough the all items
for  i in range(len(a)):
    print(a[i],end=" ,")