#Amstrong
def amstrong(num):
    temp=num
    sum=0
    while temp!=0:
        rem=temp%10
        sum=sum+rem**3
        temp=temp//10
    if num==sum: return f"{num} is an amstrong number"
    else: return f"{num} is not an amstrong number"

num=int(input("Enter the number : "))
print(amstrong(num))