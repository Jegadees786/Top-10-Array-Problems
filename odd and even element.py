arr=[]
items=int(input("Enter no.of elements in array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)

oddarr=[]
evenarr=[]

for i in range(len(arr)):
    if(arr[i] % 2 == 0):
        evenarr.append(arr[i])
    else:
        oddarr.append(arr[i])

print("The odd element array is: ",oddarr)
print("The even element array is: ",evenarr)
