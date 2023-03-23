def power(n):
    a = [int(input(f"Enter the element {i+1} :")) for i in range(n)]
    p = int(input("Enter power element :"))
    list1 = [i**p for i in a]
    print(f"power {p} of each element :\n", list1)


power(n=int(input("Enter the number of elements in list :")))
