import math


def f(arr):
    res = 0
    res_count = 0
    r = 2
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if i != j:
                if get_s(arr[i]) >= get_s(arr[j]):
                    if arr[i][r] > distance_centers(arr[i], arr[j]) + arr[j][r]:
                        count += 1
        if count >= res_count:
            if get_s(arr[i]) >= get_s(arr[res]):
                res = i
                res_count = count

    if res_count == 0:
        return 'Ничего не подходит'
    return f'Номер круга: {res + 1}, его характеристики: {arr[res]}, вмещает кругов: {res_count}'


def get_s(circle):
    return math.pi * circle[2]**2


def distance_centers(circle1, circle2):
    return math.sqrt(abs(circle1[0] - circle2[0])**2 + abs(circle1[1] - circle2[1])**2)

if __name__ == '__main__':
    # [centre_x, centre_y, radius]
    circles = [[0, 0, 7],
               [1, 1, 1],
               [0, 4, 8],
               [0, 0, 1]]
    print(f(circles))