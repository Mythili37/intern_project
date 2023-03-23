#Prime
def prime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0: c+=1
    if c==2: return f"{num} is a prime number"
    else: return f"{num} is not a prime number"

num=int(input("Enter the number : "))
print(prime(num))