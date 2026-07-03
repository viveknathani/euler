max_so_far = 0

for a in range(1, 100):
  for b in range(1, 100):
    exp = a ** b
    digit_sum = sum(int(digit) for digit in str(exp))
    if digit_sum > max_so_far:
      max_so_far = digit_sum

print(max_so_far)
