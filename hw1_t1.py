n = int(input())

x0, x1 = 0, 1

for _ in range(n):
	x0, x1 = x1, x0 + x1

print(x0)