def crit(x):
    return x > 10


def remove_if(arr, crit):
    '''Remove elements in place'''
    good = 0 # good arrays
    for i in range(len(arr)):
        if crit(arr[i]):
            arr[good] = arr[i]
            good += 1
    return arr[:good]


if __name__ == "__main__":
    arr = [i for i in range(20)]
    print("Original: ", arr)
    print("Remove_if: ", remove_if(arr, crit))

