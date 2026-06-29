def bubbleSort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


n = int(input("Enter the size of the array: "))

arr = list(map(int, input("Enter the elements: ").split()))

print("Sorted Array:", bubbleSort(arr))