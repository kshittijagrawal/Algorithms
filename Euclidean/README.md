**Euclidean Algorithm** is just an efficient way for computing Greatest Common Divisor (GCD) of two integers. Knowing to compute GCDs efficiently can be important. One of its many applications is in *cryptography*.  
### Naive Algorithm  

GCD of 2 integers is the largest number that divides both the integers with a remainder of 0. A naive approach can be running a for loop and checking the divisibility one-by-one.  
```
best = 0
for d from 1 ---> min(a, b):
  if d/a and d/b:
    best ---> d
return best
```

Rnnign
