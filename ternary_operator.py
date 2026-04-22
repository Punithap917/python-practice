x=10
y=20
max_value=x if x>y else y
print(max_value)

age=18
message="eligible to vote" if age>=18 else "not eligible to vote"
print(message)

a,b,c=3,6,9
result="a is largest" if a>b and a>c else "b is largest" if b>c else "c is largest"
print(result)

def check_even_or_odd(number):
    return "even" if number%2==0 else "odd"
print(check_even_or_odd(4))
print(check_even_or_odd(7))
