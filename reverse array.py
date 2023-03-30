arr=[]
items=int(input("Enter no.of elements in array: "))
for i in range(0,items):
    ele=int(input())
    arr.append(ele)

print(arr)

start=0
end=len(arr)-1

while(start<end):
    arr[start],arr[end]=arr[end],arr[start]
    start +=1
    end -=1

print("The reversed array is:",arr)