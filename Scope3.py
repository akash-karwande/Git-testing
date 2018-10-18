x = 67

def fun():
    # global x or we need to use return keyword
    x =2000
    return x
print("Before function call ",x)
x = fun()
print("After the function call ",x)
