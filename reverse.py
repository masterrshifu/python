def reverse(arr,N):
    start = 0
    end = N-1

    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr



list = [1,2,3,4,5,6,7]
length = len(list)

print(reverse(list, length))