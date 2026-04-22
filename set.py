my_set={1,2,3,3,4}
my_set.remove(3)
my_set.add(8)
print(my_set)

another_set=set([3,4,5,6])
print(another_set)

print(my_set | another_set)
print(my_set & another_set)
print(my_set - another_set)
print(my_set  ^ another_set)