import math

def seive(n):
  primes = [True] * (n + 1)
  primes[0] = primes[1] = False

  limit = int(math.isqrt(n)) + 1
  for i in range(2, limit):
    if primes[i]:
      for j in range(i * i, n + 1, i):
        primes[j] = False
  
  return primes

def search(n, family_count):
    is_prime = seive(n)

    for i in range(2, n + 1):
        if not is_prime[i]:
            continue

        string = str(i)
        num_digits = len(string)

        for mask in range(1, 1 << num_digits):
            selected = [string[pos] for pos in range(num_digits) if mask & (1 << pos)]

            if len(set(selected)) != 1:
                continue

            family = []

            for replacement in range(10):
                chars = list(string)

                for pos in range(num_digits):
                    if mask & (1 << pos):
                        chars[pos] = str(replacement)

                if chars[0] == "0":
                    continue

                candidate = int("".join(chars))

                if candidate <= n and is_prime[candidate]:
                    family.append(candidate)

            if len(family) >= family_count and i == min(family):
                print("base:", i)
                print("mask:", bin(mask))
                print("family:", family)
                return i

    return -1

print(search(1000000, 8))