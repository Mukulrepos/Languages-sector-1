def door_open(a):
    print(a)
    
    
    
door_open(2+1)



# types of function in python 

#  default arguments
def default(x = 10, y = 90): #it  can be change because it is default after the argument is call it can be changed
    print("result is ->",x+y)
    
default(100,200)
default()



# keyword arguments 
# it can passed the variable in a sequence by sequence using th function/block of arguments name

def keyword(x,y):
    print("result is ->",x-y)
    
    
keyword(y=10,x=9)
keyword(x=9,y=100)
# keyword()


# variable lenght function 

# it can work like a array it can point all the number in point the arry with special symbol is use (*variable name)

def variable(*x):
    for i in x :
        print(i)
        
        
variable(1,2,3,4,5,6,7,8,9)


