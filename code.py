n = 1000
ans = n
while n > 1:
    ans = ans * n + 1
    ans = ans ** 0.5
    n -= 1
print(ans)