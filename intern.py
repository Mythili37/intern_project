def default_function():
    print("Hello! Welcome to Menu driven Program")

def div(a, b):
    print(a / b)
if __name__ == "__main__":

    print("0. Exit")

    print("1. Default Choice")
    print("5. Division")

    while True:

        choice = int(input("Enter a choice"))

        if not choice:
            break

        if choice == 1:
            default_function()
        elif choice == 5:
            inp1 = int(input("enter the number"))
            inp2 = int(input("enter the number"))
            div(inp1,inp2)

    print("Thanks! Come Again")