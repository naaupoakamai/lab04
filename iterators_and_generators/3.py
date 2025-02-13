def hz_list(n):
    list=[]
    for i in range(1,n+1,):
        if i%3==0 and i%4==0:
            list.append(i)
    print(list)

n=int(input())
hz_list(n)