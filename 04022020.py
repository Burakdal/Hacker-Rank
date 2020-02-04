
def minimumBribes(q):
    count=0
    new_q=[p-1 for p in q]
    for i,p in enumerate(new_q):
        if p-i>2:
            print('Too chaotic')
            return
        for l in range(max(p-1,0),i):
            if new_q[l]> p:
                count+=1

    print(count)

def arrayManipulation(n,queries):
    total_arr=[0]*(n+1)
    for index in range(len(queries)):
        a=queries[index][0]
        b = queries[index][1]
        k = queries[index][2]
        total_arr[a-1]+=k
        if b<=len(total_arr):
            total_arr[b]-=k
    print(total_arr)
    x=max1=0
    for el in total_arr:
        x=x+el
        if x>max1:
            max1=x
    return max1

def minimumSwaps(arr):
    count=0
    index=0
    norm_arr=[i-1 for i in arr]
    index_dict={a: i for i, a in enumerate(norm_arr)}
    while index<len(arr):
        if norm_arr[index]==index:
            index+=1
            continue
        other_part_min_index=index_dict[index]
        norm_arr[index], norm_arr[other_part_min_index] = norm_arr[other_part_min_index], norm_arr[index]
        index_dict[index],index_dict[norm_arr[other_part_min_index]]=index_dict[norm_arr[other_part_min_index]],index_dict[index]
        count += 1
    return count
#dictionary indexing deneme 10 üzeri 6 da 4 kat daha yavaş brutforce indexing den
import time
test_array=[i for i in range(1000000)]
print(time.time())
dictionary={a: i for i, a in enumerate(test_array)}
print(time.time())

print(time.time())
print(test_array.index(99999))
print(time.time())


