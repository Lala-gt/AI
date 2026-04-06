def pow_fast(a, n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0: return 1
    if n == 1: return a
    t = pow_fast(a, n // 2)
    if n % 2 == 0:
        return t * t
    else:
        return a * t * t

print(pow_fast(2, 10))
