from itertools import combinations

arry = []
nele = int(input('Number of elements in array : '))
print('Enter the array elements : ')
for i in range(0,nele):
    ele = int(input())
    arry.append(ele)
sum = int(input('Enter the sum which is to be compared : '))    
com_list = []
ans = 0
comb = combinations(arry,3)

for i in list(comb):
    ref = i[0] + i[1] + i[2]
    if ref == sum:
        ans += 1
        com_list.append(i)
    print(i)

print('Number of combinations which add upto ',sum,' are : ',ans)
print('which are : ',com_list)
