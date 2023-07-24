A = [1,1,2,2,1,3,3,2,1]

ans = []

flag = False

for i in range(len(A)):
    for j in range(len(ans)):
        if(A[i] == ans[j]):
            flag = True
    
    if(flag == False):
        ans.append(A[i])
    
    flag = False


print(ans)
