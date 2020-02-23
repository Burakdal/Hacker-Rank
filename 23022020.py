#Luck Balance
#den_ar=[[5,1],[1,1],[4,0]]
def luckBalance(k, contests):
    def isImportant(contest):
        return contest[1]==1
    def isNotImportant(contest):
        return contest[1]==0
    not_important_contests=list(filter(isNotImportant,contests))
    important_contests=list(filter(isImportant,contests))
    count=0
    important_contests.sort()
    print(important_contests)
    for index,contest in enumerate(reversed(important_contests)):
        if index<k:
            count+=contest[0]
        else:
            count-=contest[0]
    for contest in not_important_contests:
        count+=contest[0]
    return count


#Greedy Florist
den_arr=[1,3,5,7,9]
k=3
def getMinimumCost(k, c):
    peoples_count=k
    flowers=c
    flowers.sort()
    cost=0
    for index,price in enumerate(reversed(flowers)):
        multiplier=(index//peoples_count)+1
        cost+=multiplier*price
    return cost
print(getMinimumCost(k,den_arr))





