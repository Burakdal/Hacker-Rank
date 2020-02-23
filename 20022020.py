

#Minimum Absolute Difference in an Array



def minimumAbsoluteDifference(arr):
    arr.sort()
    array_length = len(arr)
    minimum=abs(arr[0]-arr[1])
    i=0
    while i<array_length-1:
        if abs(arr[i]-arr[i+1])<minimum:
            minimum=abs(arr[i]-arr[i+1])
        i+=1


import time
my_ar=[-59 ,-36 ,-13, 1, -53, -92, -2, -96, -54, 75]
print(minimumAbsoluteDifference(my_ar))
start=time.time()
print(sorted(my_ar))
end=time.time()
diff1=end-start
print(min(my_ar))
print(max(my_ar))
print(abs(max(my_ar)-min(my_ar)))


