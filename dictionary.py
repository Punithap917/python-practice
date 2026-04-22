my_dict={"name":"puni","age":21,"city":"Svg"}
print(my_dict)
print(my_dict["name"])
my_dict["reg_no"]=28
my_dict["age"]=25
my_dict.pop("city")
my_dict.popitem()
del my_dict["name"]
my_dict.clear()
print(my_dict)

another_dict=dict(name="velu",age=49,city="sg")
print(another_dict)
print(another_dict.get("age"))
for key in another_dict:
    print(key)
for value in another_dict.values():
    print(value)
for key, value in another_dict.items():
    print(key,value)

my_dict.update(another_dict)
print(my_dict)

nested_dict={
             "person1":{"name":"parvathi", "age":42},
             "person2":{"name":"poona", "age":17}
             }
print(nested_dict["person1"]["name"])