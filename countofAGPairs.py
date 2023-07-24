str = ['a','b','e','g','a','g']

ans = 0
N = len(str)
for i in range(N):
    if(str[i] == 'a'):
        for j in range(i+1,N):
            if(str[j] == 'g'):
                ans += 1


print(ans)