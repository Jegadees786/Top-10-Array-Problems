arr=[]
items=int(input("Enter no.of elements for first array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)

arr1=[]
items=int(input("Enter no.of elements for second array: "))
for i in range(0,items):
    ele=int(input())
    arr1.append(ele)

print(arr1)

#intersection 
result=[]
for i in range(len(arr)):
    for j in range(0,len(arr1)):
        if(arr[i]==arr1[j]):
            result.append(arr[i])

print("The intersection elements are:",result)

#union
sum=[]
i, j = 0, 0
while i < len(arr) and j < len(arr1):
    if arr[i] < arr1[j]:
        sum.append(arr[i])  
        i += 1
    elif arr1[j] < arr[i]:
        sum.append(arr1[j])
        j+= 1
    else:
        sum.append(arr1[j])
        j += 1
        i += 1

while i < len(arr):
    sum.append(arr[i])
    i += 1

while j < len(arr1):
    sum.append(arr1[j])
    j += 1

print("The union of two array is: ",sum)