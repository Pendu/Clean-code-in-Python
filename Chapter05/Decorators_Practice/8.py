def wrapper(func):
    print("two")

    return func

@wrapper
def func():
    print("one")

def main():
    func()

if __name__=="__main__":
    main()
