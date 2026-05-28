# LOGICAL OPERATORS
print("____AND___")              #(True  True =True)
print((5>2) and (10>3))  #True   (#True  False=False)       
print((5>2) and (10<3)) #False    (#False True=False)
                                  #False False=False
print(10>5 and 8<3)      # False
print(2==2 and 3==3)     # True
print(2==2 and 3!=3)


age=19
salary=4000
print(age>19 and salary>2000) #F and T=F
print(age>18 and salary>30000) #T ana T=T

print("____OR_____")

#OR OPERATOR                           #T or T=T
print(10<5 or 8>3)       # True         F or T=T
print(10<5 or 8<3)       # False        T or F=T
print(5==5 or 7==8)      # True         F or F=F

marks=35
attendance=80
print(marks>=40 or attendance>=75)   # True

print("_____NOT_______")     #not(True)=False
                             #not(False)=True
print(not(True))
print(not(False))

age=10
print(not(age>10))
print(not(5<2))
print(not(10==10))