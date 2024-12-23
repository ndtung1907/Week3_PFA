"""
6. Nhập 2 số nguyên a và b, hãy tạo ra một tập hợp các số d là ước số chung của cả a và b
"""
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
result = set()
for i in range (1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        result.add(i)
print(result)