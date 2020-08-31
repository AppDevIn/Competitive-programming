
def reverse(str):

    #check input
    if (str == "") or len(str) < 2 :
        return "Not vaild input"
    
    str = [x for x in str]
    str.reverse()
    return ''.join(str)


if __name__ == "__main__":
    str = input()
    print(reverse(str))