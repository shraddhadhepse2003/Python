#positional argument function
'''def data(name,age,city):
    return f"My name is {name} my age is {age} and I live in {city}"
print(data('shraddha','21','thane'))
print(data('surbhi','22','ratnagiri'))'''



#key word argument
def data(name,age,city):
    return f"My name is {name} my age is {age} and I live in {city}"
print(data(age=22,name='radha',city='ratnagiri'))
