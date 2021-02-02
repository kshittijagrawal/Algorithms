import numpy as np

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
