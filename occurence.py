A = [1,2,3,3,3,4,5,5,5,5,5,6,6,6,6,6]


num = 5
count = 0

for i in range(len(A)):
    if num == A[i]:
        count += 1

print("The number of times",num,"is appearing in the list is",count)