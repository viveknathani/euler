import math

count = 0

def f(n, r):
  return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

for n in range (1, 101):
  for r in range(1, n+1):
    if f(n, r) > 1_000_000:
      count += 1

print(count)
