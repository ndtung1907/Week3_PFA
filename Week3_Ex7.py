"""
7. Nhập một dãy số nguyên từ bàn phím,
các số được viết liên tiếp, ngăn cách nhau bởi dấu chấm phẩy (;),
hãy đếm xem dãy nhập vào có bao nhiêu số khác nhau
"""
_input = list(map(int, input("Nhập một dãy số nguyên: " ).split("; ")))
result = set(_input)
print(f"Có {len(result)} số khác nhau")