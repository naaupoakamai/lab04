def squar_generetion(n):
    for i in range(1,n+1):
        yield i**2

n=int(input(""))
for square in squar_generetion(n):
    print(square)