x = "i am global variable"

def fun(x):
    print("Not assign yet so "+x)
    x = "i am local variable"
    print("After assigning, "+x)
fun(x)
print(x)
