arr=[]
items=int(input("Enter no.of elements in array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)

#selection sort algorithm
for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[min]):
            min=j
    arr[i],arr[min]=arr[min],arr[i]

print("The sorted array is:",arr)