m = 5    # number of rows
k = m-1  # number of space
c = 1    # number of star
for i in range(m):
    s = 1
    print("")
    for j in range(k):
        print(" ", end=" ")
    for z in range(c):
        print(s, end=" ")
        s+=1
    k = k-1
    c = c+2