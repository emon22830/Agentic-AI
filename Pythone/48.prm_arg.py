""""
Types of Arguments:
    1.Default Arguments
    2.POsitional Arguments
    3.Keyword Arguments
"""

#1
def power(a=2,b=3):
    return a**b

res = power(2)
print(res)



def power(a,b):
    return a**b

res = power(2,3)
print(res)


#3


def power(a,b):
    return a**b

res = power(b=2,a=3)
print(res)
