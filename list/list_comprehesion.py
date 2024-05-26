fruit=["apple","banana","cherry","kiwi","mango"]
newlist=[]
for x in fruit:
    if "a" in x :
        newlist.append(x)
        
print(newlist)

# this the append use to make a list comprehansion
# sorting list
number=[2,3,4,0,5,4,3,9,1,-1]
number.sort(reverse=True)
print(number)