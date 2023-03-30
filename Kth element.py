arr=[]
items=int(input("Enter no.of elements in array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)

k=int(input("Enter the element index number:"))

#selection sort algorithm
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[i]):
            i=j
    arr[i],arr[j]=arr[j],arr[i]

print("The element you want is",arr[k-1])