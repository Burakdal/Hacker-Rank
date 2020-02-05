#Frequency Queries
array=[[1,1],[2,2],[3,2],[1,1],[1,1],[2,1],[3,2]]
print(len(array))
from collections import defaultdict,Counter
import time

def freqQuery(queries):
    counter_Dict=defaultdict(int)
    freq=defaultdict(int)
    output_arr=[]
    for op in queries:
        val=op[1]
        fun=op[0]
        if fun==1:
            if freq[counter_Dict[val]]>0:
                freq[counter_Dict[val]]-=1
            counter_Dict[val]+=1
            freq[counter_Dict[val]]+=1
        elif fun==2:
            if counter_Dict[val]>0:
                freq[counter_Dict[val]] -= 1
                counter_Dict[val] -= 1
                freq[counter_Dict[val]]+=1
        else:
            out=0
            if freq[val]>0:
                out=1
            output_arr.append(out)
    return output_arr


print(freqQuery(array))

maydic=defaultdict(int)

print(maydic[2])


#deneme append------
import time
append_start=time.time()
deneme_ar=[]
for i in range(1000000):
    if i%2==0:
        deneme_ar.append(1)
    else:
        deneme_ar.append(0)
append_end=time.time()
difference_ap=append_end-append_start
##--------------------
#replace deneme
rep_start=time.time()
deneme2_ar=[0]*1000000
for i in range(1000000):
    if i%2==0:
        deneme2_ar[i]=1
rep_end=time.time()
difference_rep=rep_end-rep_start

print(difference_rep-difference_ap)


myset={0}
mylist=[]
start=time.time()
for i in range(1000000):
    myset.add(0)
stop=time.time()
print(stop-start)
