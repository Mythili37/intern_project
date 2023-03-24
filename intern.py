def default_function():
    print("Hello! Welcome to Menu driven Program")


if __name__ == "__main__":

    print("0. Exit")

    print("1. Default Choice")

    while True:

        choice = int(input("Enter a choice"))

        if not choice:
            break

        if choice == 1:
            default_function()

    print("Thanks! Come Again")