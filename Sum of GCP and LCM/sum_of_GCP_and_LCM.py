def find_the_higher_number(n, m):
    if n >= m:
        return n
    else:
        return m


n = int(input())
m = int(input())
LCM = 0
GCP = 0

for num in range(find_the_higher_number(n, m) + 1, -1, -1):
    if n % num == 0 and m % num == 0:
        LCM = num
        break

for num in range(1, n * m + 1):
    if num % n == 0 and num % m == 0:
        GCP = num
        break

print(GCP + LCM)
