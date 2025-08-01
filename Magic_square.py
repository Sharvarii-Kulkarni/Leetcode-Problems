def generate_magic_square(n):
    if n%2==0:
        print("Magic square requires odd number nxn matrix")
        return

    magic_square = []
    for i in range(0,n):
        row = [0]*n
        magic_square.append(row)

    num=1
    i=0
    j=n//2

    while num <= n*n:
        magic_square[i][j] = num #start adding numbers
        num = num+1

        new_i = (i-1)%n
        new_j = (j+1)%n


        if magic_square[new_i][new_j] != 0:
            i = (i+1)%n

        else:
            i = new_i
            j = new_j
    print("Magic square")
    for row in magic_square:
        for val in row:
            print(val, end=" ")
        print()



n = int(input("n: "))

sum = n*(n**2 +1)//2

generate_magic_square(n)
print(sum)