

def reverse(str):
    
    str = [x for x in str]
    str.reverse()
    print(''.join(str))


if __name__ == "__main__":
    str = input()
    reverse(str)