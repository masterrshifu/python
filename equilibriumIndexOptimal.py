def equilibriumIndex(A):

    N = len(A)
    ps = []
    ps.append(A[0])

    for i in range(1,N):
        ps.append(ps[i-1] + A[i])


    sL = 0
    sR = 0

    for i in range(N):


        if i == 0:
            sL = 0
            sR = ps[N-1] - ps[i]

        elif i == N-1:
            sR = 0
            sL = ps[i-1]

        else:
            sL = ps[i-1]
            sR = ps[N-1] - ps[i]

        if sL == sR:
            return True

    return False
