arr=[]
items=int(input("Enter no.of elements in array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)


low=0
high=len(arr)-1

while(low<=high):
    if(arr[low]<0):
        low += 1
    elif(arr[high]>0):
        high -= 1
    else:
        arr[low],arr[high]=arr[high],arr[low]

    
print("The sored array is:")    
for i in range(len(arr)):
    print(arr[i],end=" ")
