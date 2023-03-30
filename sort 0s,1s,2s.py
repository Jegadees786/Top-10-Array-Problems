arr=[]
items=int(input("Enter no.of elements in array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)

low = 0
mid = 0
high = len(arr)-1

while mid <= high:
    if arr[mid] == 0:
        arr[mid], arr[low] = arr[low], arr[mid]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print("The sorted array is:",arr)