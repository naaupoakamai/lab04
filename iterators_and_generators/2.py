def even_list(n):
    list=[]
    for i in range(0,n+1,2):
        list.append(i)
    print(list)

n=int(input())
even_list(n)
