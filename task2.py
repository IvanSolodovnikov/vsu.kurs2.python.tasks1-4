def f(ar):
    if len(ar) < 2:
        return ar
    for i in range(len(ar) - 1, -1, -1):
        marker = 0
        for j in range(1, len(ar[i])):
            if ar[i][j] < ar[i][j - 1]:
                marker = 1
                break
        if marker > 0:
            ar.append(ar.pop(i))






if __name__ == '__main__':
    arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
           [3, 2, 19],
           [5, 6, 6],
           [10, 20, 30, 40, 50, 60, 70, 80, 90],
           ]
    f(arr)
    print(*arr, sep='\n')