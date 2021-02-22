**Karatsuba Algorithm** is an efficient method used for fast multiplication of long integers or perhaps polynomials. It has a lot of applications including *error-correcting codes*, *generating functions* and *convolution in signal processing*.  
### Naive Approach
  
Let there be:  
A(x) = 3x^2 + 2x + 5  
B(x) = 5x^2 + x + 2  
A(x)B(x) = 15x^4 + 13x^3 + 33x^2 + 9x + 10  
  
The naive approach is the same way we approach similar problem in a mathematics class. Programmatically, we run a nested loop traversing through each coefficient of the functions, multiplying the coefficients, adding and placing them at their right position in the resultant array.  
```
MultPoly(A, B, n):
  product <--- Array[2n-1]
  for i from 0 to 2n-2:
    product[i] <--- 0
  for i from 0 to n-1:
    for j from 0 to n-1:
      product[i+j] <--- product[i+j] + (A[i] * B[j])
return product
```
where n = 3, A = [3, 2, 5] and B = [5, 1, 2]  
and product = [15, 13, 33, 9, 10]. (in the above example)  

The runtime of the above mentioned naive algorithm is O(n^2).  
  
### Naive Approach 2.0  
  
