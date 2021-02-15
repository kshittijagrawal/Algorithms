# funtion computing the gcd
def final_gcd(a, b):
    if b == 0:
        return a
    aa = a % b
    return final_gcd(b, aa)

# the main driver code
numbers = input()
a, b = int(numbers.split(" ")[0]), int(numbers.split(" ")[1])
res = final_gcd(a, b)
print(res)
