N = [
    [80, 158, 29],
    [162, 77, 29],
    [163, 227, 29],
    [277, 30, 16],
    [559, 433, 16],
    [276, 433, 17],
]  # Circles

array = []

for _ in range(len(N)):
    x, y = map(int, N)
    array.append((x, y))

array.sort()
array.sort(key=lambda x: x[0])


for i in array:  # 출력문
    print(*i)