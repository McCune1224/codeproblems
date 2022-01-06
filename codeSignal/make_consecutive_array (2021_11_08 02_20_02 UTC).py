def makeConsecutiveArray(inputArray):
    inputArray.sort()
    tally = 0
    for x in range(len(inputArray)-1):
        print(f" {inputArray[x]} {inputArray[x+1]}")
        if inputArray[x] + 1 != inputArray[x+1]:
            tally += inputArray[x+1] - inputArray[x] - 1
    print(tally)
    return tally
test_arr = [6,2,3,8]

def altSolution(inputArray):
    maxi = max(inputArray)
    mini = min(inputArray)
    iLen = len(inputArray)+1
    res = maxi-mini-iLen
    print(res)
    return maxi-mini-iLen
altSolution(test_arr)
