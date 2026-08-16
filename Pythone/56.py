
a = lambda X:X**2

print(a(4))


#check if a string has 'a'
a = lambda s:'a' in s
print('hello')



#Higher order function

L = [1,2,3,4,56,7]

def square(x):
    return x**2

def transform(f, L):
    output = []
    for i in L:
        output.append(f(i))
    print(output)


transform(square, L)
