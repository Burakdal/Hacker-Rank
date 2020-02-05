#ex1


def twoStrings(s1, s2):
    s1_Set=set(s1)
    s2_Set=set(s2)
    count=s1_Set.intersection(s2_Set)
    if len(count)!=0:
        return 'YES'
    return 'NO'
print(twoStrings('bruak','e'))


#ex2
from collections import Counter,defaultdict
deneme_arr=[1, 2, 2, 4]
def countTriplets(arr, r):
    triplets = 0
    m1, m2 = defaultdict(int), defaultdict(int)
    for i in reversed(arr):
        if (i * r) in m2:
            triplets += m2[i * r]
        if (i * r) in m1:
            m2[i] += m1[i * r]
        m1[i] += 1
    return triplets

from collections import defaultdict,Counter
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        print('a',a)
        b = Counter(a)
        print('b',b)
        for j in b:
            count+=b[j]*(b[j]-1)/2
    return int(count)

print(sherlockAndAnagrams('cdcd'))






