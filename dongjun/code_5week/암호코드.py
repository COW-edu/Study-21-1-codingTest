data = [0] + list(map(int, ",".join(input().strip()).split(",")))
N = len(data) - 1

if data[1] == 0:
    print("0")
else:
    cache = [0 for _ in range(N+1)]
    cache[0], cache[1] = 1, 1

    for i in range(2, N+1):
        if data[i] > 0:
            cache[i] += cache[i-1]
        if 10 <= data[i-1] * 10 + data[i] and 26 >= data[i-1] * 10 + data[i]:
            cache[i] += cache[i-2]

    print(cache[N] % 1000000)
