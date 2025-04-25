# def listSorter(listToSort: ListToSort) :
#     pass


def listSorter(array: ListToSort) -> ListToSort:
    for i in range(1, array.Length()):
        key = i
        # print('key', key)
        j = i - 1
        while j >= 0 and array.Smaller(key, j):
            array.Swap(key,j)
            j -= 1
            key -=1
            # print(array)
    return array