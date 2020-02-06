#bubble sort


def countSwaps(a):
    count=0
    for i in range(len(a)):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                count+=1
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


#max toys

def maximumToys(prices, k):
    affordable=[toy for toy in prices if toy<k]
    toyCount=0
    affordable.sort()
    for toy in affordable:
        if toy<k:
            toyCount+=1
            k-=toy
    return toyCount

#expenditures
deneme_Arr=[10,20,30,40,50,60]
print(deneme_Arr[:-1])

#count sort
def countSort(arr):
    countArr=[0]*(max(arr)+1)
    output_arr=[0]*len(arr)
    for i in arr:
        countArr[i]+=1
    for j in range(len(countArr)):
        countArr[j]=countArr[max(j-1,0)]+countArr[j]
    for k in arr:
        index=countArr[k]
        output_arr[index-1]=k
        countArr[k]-=1
    return output_arr


print(countSort([1,4,5,7,32,6,9,3]))




# Complete the activityNotifications function below.

def get_median(counts, mids):
    res = []
    for mid in mids:
        gone = 0
        for i, v in enumerate(counts):
            gone += v
            if gone >= mid:
                res.append(i)
                break
    return sum(res) / len(res)

#medianı bulmak için arrayi sort etmek gerekiyo sort işlemi built in de brutforce yada bubble ile yapılıyo.
#count sort çok daha hızlı oluyo index lere ihtiyaç olması durumunda.
def activityNotifications(expenditure, d):
    alerts = 0
    counts = [0] * 201
    if d % 2 == 1:
        mids = [d // 2 + 1]
    else:
        mids = [d // 2, d // 2 + 1]
    for v in expenditure[:d]:
        counts[v] += 1
    for i, exp in enumerate(expenditure[d:]):
        median = get_median(counts, mids)

        if exp >= 2 * median:
            alerts += 1

        old_value = expenditure[i]
        counts[old_value] -= 1
        counts[exp] += 1
    return alerts





print(activityNotifications(deneme_Arr,3))

print(int(1.5))
