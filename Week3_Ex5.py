"""
5. Nhập số nguyên N, tạo một tập hợp các số nguyên dương d là ước số của N
"""
n = int(input("Nhập n: "))
print(set(i for i in range(1, n + 1) if n % i ==0))