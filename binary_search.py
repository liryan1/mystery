def searchRange(nums: list[int], target: int) -> list[int]:
    beg, end = 0, len(nums) - 1
    # find the left index
    while beg <= end:
        mid = (beg + end) // 2
        if nums[mid] == target:
            if (mid - 1 < 0) or nums[mid - 1] < target:
                start = mid
                break
            end = mid - 1
        elif nums[mid] < target:
            beg = mid + 1
        else: # nums[mid] > target:
            end = mid - 1
    else:
        start = -1


    # find the right index
    beg, end = 0, len(nums) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if nums[mid] == target:
            if (mid + 1 >= len(nums)) or nums[mid + 1] > target:
                stop = mid
                break
            beg = mid + 1
        elif nums[mid] < target:
            beg = mid + 1
        else: # nums[mid] > target:
            end = mid - 1
    else:
        stop = -1

    return [start, stop]

if __name__ == "__main__":
    L = [5,7,7,8,8,10]
    t = 8
    print(searchRange(L, t))

    L = [1,1,1,2,2,2,2,2,2,2,3,3]
    t = 3
    print(searchRange(L, t))