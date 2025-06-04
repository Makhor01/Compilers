n, I = map(int, input().split())
a = sorted(list(map(int, input().split())))
cur = 0
b = [0]
for i in range(1, n):
    if a[i] != a[i - 1]:
        cur += 1
    b.append(cur)
r = 1
ans = int(1e18)
for l in range(len(b)):
    ma = b[l] + 2 ** min((I * 8 // n), 30) - 1
    while r < n and b[r] <= ma:
        r += 1
    ans = min(ans, l + (n - r))
print(ans)