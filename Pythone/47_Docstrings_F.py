def odd_evan(num):
    """"
    _summary_

    Args:
        num(_type_): _description_


    Returns:
        _type_: _description_
    """
    if num%2 == 0:
        return "Even Numver"
    else:
        return "Odd Number"


res = odd_evan(3)
print(res)

print(odd_evan.__doc__)

print(max.__doc__)



#another way 
def odd_evan(num):
    """"
    _summary_

    Args:
        num(_type_): _description_


    Returns:
        _type_: _description_
    """
    if type(num) == int:
        if num%2 == 0:
            return "Even Numver"
        else:
            return "Odd Number"

    else:
        return "Wrong Input"


res = odd_evan("5")
print(res)

