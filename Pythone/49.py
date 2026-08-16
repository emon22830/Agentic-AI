# #args - allows us to pass a variable number of non-keyword arguments to a function

# def multiply (a,b,c):
#     return a * b * c


# print(multiply(a=2, b=3, c=5))



# def multiply (a,b,c):
#     return a * b * c
# print(multiply(a=2, b=3, c=5))


def multiply(*args):
    product = 1
    for i in args: 
        product = product *  i

    return product


res = multiply(1,2,34,5,6,7)
print(res)



#kwargs - allow us to pass number of keyword argimets
#keyword arguments mean that they contain a key- value pair , like a  puthon dictoniary 

def display(**kwargs):
     for (key, value) in kwargs.items():
         print(f"{key} -> {value}")



res = display(india="Delhi", Bangladesh="Dhaka")

print(res)
