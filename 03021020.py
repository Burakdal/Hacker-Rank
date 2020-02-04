#ex1111
import random
clouds=[0,0,0,1,0,0]
def findJumps(array):
    steps=0
    i=0
    while i+1<len(array):
        second=array[i+1]
        third = 0 if i+2==len(array)else array[i + 2]
        if (second==0 and third==0) or (second==1 and third==0):
            i+=2
        else:
            i+=1
        steps += 1

#ex222
def repeatedStrings(n,s='aba'):
    total_repeat=n//len(s)
    sub_count=s.count('a')
    total_repeat_count=sub_count*total_repeat
    additional_part=n%len(s)
    additional_part_count=s[:additional_part].count('a')
    return total_repeat_count+additional_part_count

s='aba'
n=20
print(repeatedStrings(n,s))

#ex3333

s='DUDUDUDU'
n=8
def valleyCount(n,s):
    altitude=0
    valley_c=0
    for path in s:
        n_path=-1 if path=='D' else 1
        is_before_above_See = True if altitude>=0 else False
        altitude+=n_path
        if is_before_above_See and altitude<0:
            valley_c+=1
    return valley_c

print(valleyCount(n,s))


#EX4

def createArray():
    my_Arr=[]
    for i in range(6):
        my_Arr.append([random.randint(-9, 9) for j in range(6)])
    return my_Arr


def maxHourGlassValue(arr):
    array_len=len(arr)
    hourGlassValues=[]
    for row in range(1,array_len-1):
        for col in range(1,array_len-1):
            self = arr[row][col]
            upper_part = arr[row - 1][col - 1] + arr[row - 1][col] + arr[row - 1][col + 1]
            lower_part = arr[row + 1][col - 1] + arr[row + 1][col] + arr[row + 1][col + 1]
            glassvalue = self + upper_part + lower_part
            hourGlassValues.append(glassvalue)
    return max(hourGlassValues)
array=createArray()
print(maxHourGlassValue(array))

#ex55

def rotLeft(a, d):
    first_range=range(0,len(a))
    last_range=range(0-d,len(a)-d)
    new_array=[0]*len(a)
    for i,j in zip(last_range,first_range):
        new_array[i]=a[j]
    return new_array

#ex6
array=[2, 5, 1, 3, 4]
def minimumBribes(q):
    count=0
    invalid=False
    counted_indexes=[]
    for index in range(len(q)):
        real_val=index+1
        index_val=q[index]
        diff=index_val-real_val
        if diff>0:
            count+=diff
        if diff>2:
            print('Too chaotic')
            invalid=True
        if diff==0 :
            before=q[index-1]-real_val-1
            after=q[index+1]-real_val+1
            if before+after==0:

                if q[index] not in counted_indexes:
                    counted_indexes.append(q[index])
                    count += 1
        if diff<-2:
            if q[index] not in counted_indexes:
                counted_indexes.append(q[index])
                count += 1
    if not invalid:
        print(count)

minimumBribes(array)

def oldOne(q):
    swapped_indexes = []
    true_q = list(range(min(q), max(q) + 1))
    three_bribe = False
    remaining_index = 0
    while True:
        if three_bribe:
            break
        if true_q == q:
            break
        for i in range(remaining_index, len(q)):
            if i + 1 != len(q):
                first = q[i]
                second = q[i + 1]
                if first < second:
                    if second == i + 1:
                        remaining_index = i + 1
                    continue
                if swapped_indexes.count(first) < 2:
                    q[i] = second
                    q[i + 1] = first
                    swapped_indexes.append(first)
                else:
                    three_bribe = True
    if three_bribe:
        print('Too chaotic')
    else:
        print(len(swapped_indexes))
minimumBribes(array)





















