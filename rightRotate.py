A = [1, 2, 3, 4, 5]

B = len(A)
C = 2

start = 0
end = B-1

while(start < end):
    A[start], A[end] = A[end], A[start]
    start = start + 1
    end = end - 1

print(A)
    
start = 0
end = C-1

while(start < end):
    A[start], A[end] = A[end], A[start]
    start = start + 1
    end = end - 1

print(A)

start = C
end = B-1

while(start < end):
    A[start], A[end] = A[end], A[start]
    start = start + 1
    end = end - 1

print(A)

for i in range(0, B-2):
    if list[i]>C+1:
        list[i] = list[i] - C
    else:
        list[i] = list[i] + C +1

print(A)
