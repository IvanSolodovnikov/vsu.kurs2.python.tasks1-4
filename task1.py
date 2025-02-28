def f(arr):
    if len(arr) < 2:
        return arr
    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            res.append(arr[i])
    return res

if __name__ == '__main__':
    arr1 = [1,2,3,2,3,3,2]
    arr2 = f(arr1)
    print(arr1, arr2, sep='\n')