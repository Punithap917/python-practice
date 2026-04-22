def add_num(a, b):
    return a+b
result=add_num(5,10)
print(result)

def calculate(a, b):
    return a+b,a-b,a*b,a/b
add,sub,mul,div=calculate(10,5)
print(add,sub,mul,div)

def greet(name):
    return f"Hello,{name}!" #using f-string
print(greet("punitha"))

def greet(name="guest"):
    return f"Hello,{name}!"
print(greet())
print(greet("punitha"))

square=lambda x:x**2
print(square(5))

# *hobbies positional arguments...collected into tuple
# **details key-value pair...collected into dictionary
def describe_person(name,*hobbies,**details):
    print(f"name:{name}")
    print(f"Hobbies:{','.join(hobbies)}")
    print(f"details:{details}")
describe_person("john", "dancing", "sleeping", age=21, city="svg")