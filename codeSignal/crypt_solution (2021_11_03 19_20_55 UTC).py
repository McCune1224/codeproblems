def isCryptSolution(crypt: list, solution: list):
    value_list = [[]]* len(crypt)
    for idx, word in enumerate(crypt):
        value_str = ""
        print(f"Checking {word}")
        for letter in word:
            for idx, pair in enumerate(solution):
                print(pair[0])
                if pair[0] == letter:
                    print(f"match at i:{idx}, '{letter}'")


    


if __name__ == "__main__":
    

    crypt1 =  ["SEND", "MORE", "MONEY"]
    solution1 = [["O","0"], ["M","1"], ["Y","2"], ["E","5"], ["N","6"], ["D","7"], ["R","8"], ["S","9"]]

    
    crypt2 =  ["TEN", "TWO", "ONE"]
    solution2 = [["O","1"], ["T","0"], ["W","9"], ["E","5"], ["N","4"]]

    print(isCryptSolution(crypt1,solution2))
    print(isCryptSolution(crypt1,solution2))
