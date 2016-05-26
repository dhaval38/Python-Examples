no_primes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
print no_primes
primes = [x for x in range(2, 100)if x not in no_primes]
print primes
