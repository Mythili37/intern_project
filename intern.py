def default_function():
    print("Hello! Welcome to Menu driven Program")

def add(a,b):
    print(a+b)
def mul(a,b):
    print(a*b)

def div(a, b):
    print(a / b)
if __name__ == "__main__":

    print("0. Exit")

    print("1. Default Choice")
    print("2. Addition")
    print("4.Muiltiplication")
    print("5. Division")

    while True:

        choice = int(input("Enter a choice"))

        if not choice:
            break

        if choice == 1:
            default_function()
        elif choice == 2:
            inp1 = int(input("enter the number"))
            inp2 = int(input("enter the number"))
            add(inp1,inp2)
        elif choice==4:
            inp1 = int(input("enter the number"))
            inp2 = int(input("enter the number"))
            mul(inp1,inp2)
        elif choice == 5:
            inp1 = int(input("enter the number"))
            inp2 = int(input("enter the number"))
            div(inp1,inp2)

    print("Thanks! Come Again")