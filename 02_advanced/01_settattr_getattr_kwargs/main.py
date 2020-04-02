def what_are_the_vars(*args, **kwargs):
    ret = ObjectC()
    for c, value in enumerate(args):
        setattr(ret, ("var_" + str(c)), value)
    for key, value in kwargs.items():
        if key in dir(ret):
            return 
        else: 
            setattr(ret, key, value)
    return ret


class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_': # to filter out builtin attributes
            value = getattr(obj, attr)
            print(f"{attr}: {value}")
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world") # var_0 already exists
    doom_printer(obj)