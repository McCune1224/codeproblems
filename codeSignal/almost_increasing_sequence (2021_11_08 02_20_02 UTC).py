def almostIncreasingSequence(sequence):
    print(sequence)
    if len(sequence) ==2:
        return True
    found_bad_pair = -1 
    for i in range(len(sequence)-1):
        if sequence[i] > sequence[i+1]:
            found_bad_pair = i
            print(f"bad number at index {i}")
            break
    if found_bad_pair == -1:
        return True
    
        
            

test1 = [1,3,2,1]
test2 = [1,3,2]
print(almostIncreasingSequence(test1))
#print(almostIncreasingSequence(test2))
