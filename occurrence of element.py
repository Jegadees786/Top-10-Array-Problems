arr=[]
items=int(input("Enter no.of elements in array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)
search=int(input("Enter the element to find the occurrence:"))
count=0
for i in range(len(arr)):
    if(search==arr[i]):
        count +=1

print("The element occur in",count,"times")