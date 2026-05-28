# identity operators
print("______is__________")
num=10
num_1=num
print(num is num_1)

x=10
y=10
print(x is y)

x="suchi"
y="bhavya"
print(x is y)

x="suchi"
y="suchi"
print("suchi" is "suchi")

print("___________is not_______")

x="suchi"
y="bhavya"
print(x is not y)

x=10
y=20
print(x is not y)
 
num_1=10
num_2=10
print(num_1 is not num_2)