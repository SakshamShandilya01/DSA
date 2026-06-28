def findLargest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


n = int(input())
arr = list(map(int, input().split()))

print(findLargest(arr))