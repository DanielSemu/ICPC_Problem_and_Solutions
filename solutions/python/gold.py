
import math
MAX = 10000;


primes = [];
def sieveSundaram():
	
	marked = [False] * (int(MAX / 2) + 100);
	for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
		for j in range((i * (i + 1)) << 1,
						int(MAX / 2) + 1, 2 * i + 1):
			marked[j] = True;
	primes.append(2);
	for i in range(1, int(MAX / 2) + 1):
		if (marked[i] == False):
			primes.append(2 * i + 1)
def findPrimes(n):
	
	if (n <= 2 or n % 2 != 0):
		
		return;
	i = 0;
	while (primes[i] <= n // 2):
	
		diff = n - primes[i];
		if diff in primes:
			
			print(primes[i],  diff);
			return;
		i += 1;
sieveSundaram();

while(True):
	x=int(input())
	if x==-1:
		break
	print(findPrimes(x))
