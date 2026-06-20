a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

if(a is c):
    print("True")
else:
    print("False")

if(a is b):
    print("True")
else:
    print("False")

x = 24
y = 24

if(x is not y):
    print("True")
else:
    print("False")

if(type(x) is int):
    print("x IS AN INTEGER")
else:
    print("NOPE")