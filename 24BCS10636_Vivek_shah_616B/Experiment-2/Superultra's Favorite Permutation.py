t = int(input())

for _ in range(t):
    n = int(input())

    if n <= 3:
        print(-1)
        continue

    num=[i for i in range(2,n+1,2)]
    num2=[j for j in range(1,n+1,2)]
    ans=num+num2

    print(*ans)
