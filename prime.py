def isPrime(N):

    count = 0
    for i in range(1,N+1):
        if(N%i == 0):
            count += 1
    if(count == 2):
        return True
    return False 
    

print(isPrime(4))
print(isPrime(7))
print(isPrime(71))
print(isPrime(72))
print(isPrime(37))