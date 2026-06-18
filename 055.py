def is_palindrome(n):
  if n < 0:
    return False
  return str(n) == str(n)[::-1]

def rev(n):
  if n < 0:
    return -1
  return int(str(n)[::-1])

def check(n):
  iterations = 0

  num = n
  
  while True:
    if iterations >= 50:
      break
    
    res = num + rev(num)

    if is_palindrome(res):
      return False
    
    num = res
    
    iterations += 1

  return True

count = 0

max_check_till = 10_000

for i in range(0, max_check_till + 1):
  if check(i):
    count += 1

print(count)
