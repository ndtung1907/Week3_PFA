"""
2. Tạo một tập hợp gồm các số nguyên lẻ trong khoảng từ 1 đến 199, in chúng ra màn hình
"""
result = {i if i%2!=0 else 1 for i in range (200)}
print(result, end=" ")