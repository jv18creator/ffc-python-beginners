class JustNotCoolError(Exception):
    pass


x = 2
try:
    raise JustNotCoolError("Not cool man!")
    # raise Exception("I'm a custom exception!")
    # print(x / 2)
    # if type(x) is not str:
    #     raise TypeError("Only strings are allowed")
except NameError:
    print("NameError means something is probably undefined")
except ZeroDivisionError:
    print("Cant devide by zero")
except Exception as error:
    print(error)
else:
    print("No errors!")
finally:
    print("Reached finally")
