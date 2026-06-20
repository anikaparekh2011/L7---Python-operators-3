test1 = int(input())
test2 = int(input())
test3 = int(input())
test4 = int(input())

total = test1 + test2 + test3 + test4

avg = int(total/4)
validrange = range(50, 101)

if avg in validrange:
    print("PASS")
else:
    print("FAIL")
    

