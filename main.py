def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    high1, low1 = x // 10**m, x % 10**m
    high2, low2 = y // 10**m, y % 10**m
    
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)
    
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

if __name__ == "__main__":
    num1 = 12345678901234567890
    num2 = 98765432109876543210

    result = karatsuba(num1, num2)
    print(f"O resultado da multiplicaçãp de {num1} por {num2} é: {result}")