## live laugh love bad code
file = open("input.txt","r").read().split()

list1 = [int(file[i]) for i in range(len(file)) if i%2==0]
list2 = [int(file[i]) for i in range(len(file)) if i%2==1]
## part one
## list1.sort()
## list2.sort()
## thenumberrrrr = 0
## for i in range(len(list1)):
##     thenumberrrrr+=(abs(list1[i]-list2[i]))
##
## print(thenumberrrrr)

## part two
numbertwoo = 0
for i in range(len(list1)):
    numbertwoo += (list2.count(list1[i])*list1[i])

print(numbertwoo)
