def sum_zero(A):

    elements = set
    sum = 0

    for i in range(len(A)):
        sum += A[i]

        if sum == 0 or sum in elements:
            return True
        else:
            elements.add(sum)

    
    return False

A = [1,-1,2,3]
print(sum_zero(A))