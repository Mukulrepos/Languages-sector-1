language=["hindi","english","German","japanese"]
print(language[3-3])
if "hindi" in language:
    print("okey")
else:
    print("sorry")
    
items=[i for i in range(10) if i%2==0 ]
print(items)

language.append(12) #Used for adding elements to the end of the List. 
print(language)
bhasa=language.copy()# copy the list items in the new items areas

print(bhasa)
# language.clear()#clear the items from the list
# print(language)

fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")

print(x)


other_language=["marthi","bihari"]

language.extend(other_language)
print(language)


language.insert(2,"pagal")
print(language)