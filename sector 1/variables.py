locators=int(input("enter the dynamic location in meter  "))
if locators>=100:
    print("Is to faar 100m above",locators,"m")
elif locators>= 80:
    print("is near in 80 m to ",locators,"m")
elif locators>= 60:
    print("is near in 60 m to ",locators,"m")
elif locators>= 40:
    print("is near in 40 m to ",locators,"m")
elif locators>= 20:
    print("is near in 20 m to ",locators,"m")
else:
    print("Is very close you position")
    