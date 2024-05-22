age = int(input("Enter your age, please: "))
licenses = int(input("Enter your license number: "))

if age >= 20 and licenses == 123:
    print("Thank you, sir.")
    winename = input("Enter your wine name: ")
    match winename:
        case "rock":
            print("Thank you, sir.")
        case "redwine":
            print("Thank you, sir.")
        case _:
            print("This wine is not available.")

else:
    print("sorry sir ")
    if age>=18 :
        print("Ghar ja ka padhi kar ")