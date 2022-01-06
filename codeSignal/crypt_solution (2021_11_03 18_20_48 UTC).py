def isCryptSolution(crypt: list, solution: list):
    value_list = [[]]* len(crypt)
    for idx, word in enumerate(crypt):
        str_value = ""
        print(idx, word)
        print(word[0])
        print(solution.index(word[0]))
        #if solution[solution.index(word[0])][0] == "0":
        #    return False
        for letter in word:
            pass
#            print(letter)
            

    


if __name__ == "__main__":
    

    crypt1 =  ["SEND", "MORE", "MONEY"]
    solution1 = [["O","0"], ["M","1"], ["Y","2"], ["E","5"], ["N","6"], ["D","7"], ["R","8"], ["S","9"]]

    
    crypt2 =  ["TEN", "TWO", "ONE"]
    solution2 = [["O","1"], ["T","0"], ["W","9"], ["E","5"], ["N","4"]]

    print(isCryptSolution(crypt1,solution2))
    print(isCryptSolution(crypt1,solution2))
