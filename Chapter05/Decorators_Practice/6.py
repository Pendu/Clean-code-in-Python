# A Python example to demonstrate that
# decorators can be useful attach data

# A decorator function to attach
# data to func
def attach_data(func):
	func.data = 3
	return func

@attach_data
def add (x, y):
	return x + y


# Driver code

def main():
    # This call is equivalent to attach_data()
    # with add() as parameter
    print(add(2, 3))

    print(add.data)

if __name__=="__main__":
    main()