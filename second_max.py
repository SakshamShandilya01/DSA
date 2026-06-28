def secondLargest(arr):
    largest = arr[0]
    second = -1

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and (second == -1 or num > second):
            second = num

    return second


n = int(input())
arr = list(map(int, input().split()))

print(secondLargest(arr))