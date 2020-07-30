condition = True


def conditional_decorator(func):
    def wrapper():
        oldstring = func()

        if condition:
            newstring = oldstring.upper()
        else:
            newstring = oldstring.lower()

        return newstring

    return wrapper


@conditional_decorator
def func():
    return 'geeKSfoRGEEks'

def main():

    print(func())

if __name__== "__main__":
    main()