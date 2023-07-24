def repeatingElement(A,n):

    elements = {}

    for value in A:
        if value in elements:
            elements[value] += 1
        else:
            elements[value] = 1


    for i in range(n):
        if elements.get(A[i]) > 1:
            return A[i]
        


A = [2,1,1,2,1,2,3,3,1,3,3]

N = len(A)

print(repeatingElement(A, N))