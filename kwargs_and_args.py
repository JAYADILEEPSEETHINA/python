# args takes no of arguments .
#args will converted to tuple
def add(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
add(10,20,40,80)
#kwargs many keywords argument .it takes in dictioary type
def calcualte(**kwargs):
    print(kwargs)
    name=kwargs.get("name")#get to be used when not provide value.it return none
    print(name)

calcualte(add=3,mul=34)