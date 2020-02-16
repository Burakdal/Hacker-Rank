#sorting problem
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return "Player"

    def comparator(self,a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.score == b.score:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            else:
                return 0


#countInversions
import random
array=[random.randint(0,100) for i in range(100)]
def mergeSort(arr):
    count=0
    mid = len(arr) // 2  # Finding the mid of the array
    L = arr[:mid]  # Dividing the array elements
    R = arr[mid:]  # into 2 halves
    if len(arr)>1:
        count+=mergeSort(L)  # Sorting the first half
        count+=mergeSort(R)  # Sorting the second half
    i = j = k = 0
    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            if arr[k]!=L[i]:
                count+=1
            arr[k] = L[i]
            i += 1
        else:
            if arr[k]!=R[j]:
                count+=1
            arr[k] = R[j]
            j += 1
        k += 1
    # Checking if any element was left
    while i < len(L):
        if arr[k] != L[i]:
            count += 1
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        if arr[k] != R[j]:
            count += 1
        arr[k] = R[j]
        j += 1
        k += 1
    return count



array1=[1,34,6,8,3,2,5,7,9,0,4,5,67,2,4,7]
print(mergeSort(array1))


def merge(arr, left_half, right_half):
    i, j, k = 0, 0, 0
    inversions = 0
    left_len, right_len = len(left_half), len(right_half)
    while i < left_len and j < right_len:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            inversions += left_len - i
        k += 1

    while i < left_len:
        arr[k] = left_half[i]
        i, k = i+1, k+1

    while j < right_len:
        arr[k] = right_half[j]
        j, k = j+1, k+1

    return inversions

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half, right_half = arr[:mid], arr[mid:]
        inversions = merge_sort(left_half) + merge_sort(right_half) + merge(arr, left_half, right_half)
        return inversions
    return 0
def countInversions(arr):
    return merge_sort(arr)


#minimum number of deletion for make them anagrams

from collections import Counter
print(Counter("burakfafka"))
def makeAnagram(a,b):
    counter_a=Counter(a)
    counter_b=Counter(b)
    count=0
    for key,val in counter_a.items():
        if key not in counter_b:
            count+=val
        else:
            if val<counter_b[key]:
                continue
            count+=val-counter_b[key]
    for key,val in counter_b.items():
        if key not in counter_a:
            count+=val
        else:
            if val<counter_a[key]:
                continue
            count+=val-counter_a[key]
    return count

#find the count of deletion to prevent adjent

def alternatingCharacters(s):
    counter=0
    i=0
    while i<len(s) and i+1!=len(s):
        if s[i]==s[i+1]:
            counter+=1
        i+=1
    return counter


print(alternatingCharacters("bbbdeeelldgu"))

#Sherlock and the Valid String
from collections import Counter
def isValid(s):
    counter_s=Counter(s)
    counter_values=Counter(list(counter_s.values()))
    counter_values_keys=list(counter_values.keys())
    if len(counter_values)<3:
        if len(counter_values)==1:
            return "YES"
        control_1=abs(counter_values_keys[0]-counter_values_keys[1])<2
        if 1 in counter_values.values() and control_1:
            return "YES"
    return "NO"

#Special String Again

def substrCount(n, s):
    tot = 0
    count_sequence = 0
    prev = ''
    for i,v in enumerate(s):
        count_sequence += 1
        if i and (prev != v):
            j = 1
            while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
                if s[i-j] == prev == s[i+j]:
                    tot += 1
                    j += 1
                else:
                    break
            count_sequence = 1
        tot += count_sequence
        prev = v
    return tot
from collections import Counter
def commonChild(s1, s2):
    if s1==s2:
        return len(s1)-1
    s1_counter=Counter(s1)
    s2_counter=Counter(s2)
    counter=0
    common=''
    for key,val in s1_counter.items():
        if key in s2_counter.keys():
            if len(common) > 0:
                condition=s1.index(common[-1]) < s1.index(key) and s2.index(common[-1]) < s2.index(key)
                if condition:
                    common += key
                    if val < s2_counter[key]:
                        counter += val
                    else:
                        counter+=s2_counter[key]
            else:
                common+=key
                if val < s2_counter[key]:
                    counter += val
                else:
                    counter += s2_counter[key]
    return counter
ex1="SHINCHAN"
ex2="NOHARAAA"
print(commonChild(ex1,ex2))
print(ex1[-1])
