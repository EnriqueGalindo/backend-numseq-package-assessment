import math


def is_prime(n): 
  pfact_list = [1]
  while n % 2 == 0: 
      pfact_list.append(2)  
      n = n / 2
  for i in range(3,int(math.sqrt(n))+1,2): 
      while n % i== 0: 
          pfact_list.append(i) 
          n = n / i 
  if n > 2: 
      pfact_list.append(n) 
  if len(pfact_list) > 2:
    return False
  return True


def primes(n):
    prime_list = []
    for i in range(1, n+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list
