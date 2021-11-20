c = [2, 1, 2, 3, 3, 4]
b = [2,1,2,3,3,4]
def divideArray(a):
    dupCheck = {}
    for i in range(len(a)):
        if a[i] not in dupCheck:
            dupCheck[a[i]] = 1

        if [a[i]] in dupCheck:
            dupCheck[a[i]] += 1
            if dupCheck[a[i]] >=3:
                print(f"{dupCheck[a[i]]} repeated more than twice")
                print(dupCheck)
                return []

    list1 = []
    list2 = []
    skip_index = 0
    for x in range(len(a)):
        if a[x] not in list1 and len(list1)*2 != len(a):
            list1.append(a[x])
    print(list1)
    

#divideArray(c)
divideArray(b)
