def mergeSort(x:list, y:list) -> list:
    x.extend(y)
    x.sort()
    return x

if __name__ == "__main__":
    print(mergeSort([0, 3, 4, 31], [4, 6, 30]))