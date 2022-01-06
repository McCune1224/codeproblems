def checkPalindrome(inputString):
    flip = inputString[::-1]
    if inputString != flip:
        return False
    return True

inp = input()
checkPalindrome(inp)
