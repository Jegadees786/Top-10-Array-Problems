arr=[]
items=int(input("Enter no.of elements in array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)

min=arr[0]
max=0
for i in range (len(arr)):
    if(min>arr[i]):
        min=arr[i]
    if(arr[i]>max):
        max=arr[i]
    
print("Minimum value in a array is: ",min)
print("Maximum value in a array is: ",max)