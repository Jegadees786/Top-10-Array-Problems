arr=[]
items=int(input("Enter no.of elements in array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)

for i in range(len(arr)-1):
    if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
        print("The peak element is:",arr[i])