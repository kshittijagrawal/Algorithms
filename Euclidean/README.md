**Euclidean Algorithm** is just an efficient way for computing Greatest Common Divisor (GCD) of two integers. Knowing to compute GCDs efficiently can be important. One of its many applications is in *cryptographic algorithms like RSA*.  
### Naive Algorithm  

GCD of 2 non-negative integers is the largest number that divides both the integers with a remainder of 0. A naive approach can be running a for loop and checking the divisibility one-by-one.  
```
best = 0
for d from 1 to min(a, b):
  if d/a and d/b:
    best <--- d
return best
```
This algorithm works just fine but with the cost of its runtime. If the input size is small, i.e a, b <= 10^2, the runtime is approximately linear. If the input scales, i.e a, b <= 10^9, the runtime too scales. Though theoretically it is linear, it could take several minutes to compute.  

### Euclidean Algorithm  

A recursive technique, here, could fill the void of runtime.  
The lemma says that `gcd(a, b) = gcd(a', b) = gcd(b, a')`, where a' is the remainder when a is divided by b.  
```
Euclid(a, b):
  if b == 0:
    return a
  a' <--- remainder when a is divided by b
  return Euclid(b, a')
```
Even if the size of the input is of the order of 10^7, the algorithm would take a maximum of 6 to 7 steps to compute the GCD, as each recursive call reduces the size of the numbers by approximately a factor of 2. Takes about log(ab) steps in general.
