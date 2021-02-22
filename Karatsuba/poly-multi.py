import numpy as np

# n is the number of terms in the quadratic eq
# a and b are the particular terms of our final result which we aim to find. During the start, they are 0 each
def poly_mult_dc_naive(A, B, n, a, b):
  C = np.zeros(2*n - 1, dtype=int)
  if n == 1:
    C[0] = A[a] * B[b]
    return C[0]
  C[0:n-1] = poly_mult_dc_naive(A, B, n//2, a, b)
  C[n:2*n-1] = poly_mult_dc_naive(A, B, n//2, a + (n // 2), b + (n // 2))
  W = poly_mult_dc_naive(A, B, n//2, a, b + (n // 2))
  V = poly_mult_dc_naive(A, B, n//2, a + (n//2), b)
  C[(n // 2) : (3*n // 2) - 1] += W + V
  return C

if __name__ == '__main__':
    print(poly_mult_dc_naive([0,3,2,5], [0,5,1,2], 4, 0, 0))

# here A(x) = 0x^3 + 3x^2 + 2x^1 + 5 ---> 3x^2 + 2x^1 + 5
# and B(x) = 0x^3 + 5x^2 + x^1 + 2 ---> 5x^2 + x^1 + 2
# which results in [0  0 15 13 33  9 10]
# i.e 0x^6 + 0x^5 + 15x^4 + 13x^3 + 33x^2 + 9x + 10 ---> 15x^4 + 13x^3 + 33x^2 + 9x + 10
