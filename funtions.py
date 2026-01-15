def greet():  #without param,eter and return
    print("hello")
    

def square(n):  #with parameter
    print(n*n)
    
def sub(a,b):  #with return
    return a-b

def operation(a,b):
    return a+b , a-b , a*b

def greets(name="user"):
    print("hello",name)
    
    

# *args  variable length argument , didnt know how many val user will send
# *packs multiple val  ,  args is just name(can be changed) , store val as tuple
def adds(*number):
    total=0
    for n in number:
        total+=n
    return total
    
# **kwarg  keyword variable argument
# value come in key val pair
# kwargs is a dictionary
def profile(**data):
    for key, value in data.items():
        print(key, ":", value)
        
        
# lambda func
# auto return
squares = lambda x: x*x

check = lambda n: "even" if n%2==0 else "odd"


nums =[1,2,3,2,5]
sq= list(map(lambda x: x*x,nums))
print(sq)




even = list(filter(lambda x: x%2==0,nums))
print (even)


def add(a,b):
    print(a+b)
    
add(5,6)
greet()
square(5)
sub(5,9)


v,w,x= operation(5,8)
print(v,w,x)

greets()
greets("anmol")


adds(5,6,45,7)

profile(name="anmol",brach="air" )


squares(10)
print(check(200))
print(check(201))




