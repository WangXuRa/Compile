def main():
    strLength = None
    print("Please enter the length of the string: ", sep='', end='')
    strLength = int(input())
    inputStr = None
    print("Please enter the string: ", sep='', end='')
    inputStr = str(input())
    midPoint = None
    midPoint = strLength / 2
    i = None
    i = 0
    while i < midPoint:
        if inputStr[i] != inputStr[strLength - 1 - i]:
            print("The string is not a palindrome.", "\n", sep='', end='')
            return 0
        (i:=i+1)
    print("The string is a palindrome.", "\n", sep='', end='')
    return 0

if __name__ == '__main__':
    main()