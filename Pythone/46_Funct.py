def greet(name):
    output = f"Hello {name}, Welcome to python"
    return output


names = ["Emon", "Maria", "Evan"]

for name in names:
    res = greet(name)
    print(res)




def odd_evan(num):
    if num%2 == 0:
        return "Even Numver"
    else:
        return "Odd Number"


res = odd_evan(3)
print(res)


for i in range(1,11):
    res =(odd_evan(i))
    print(i, res)
