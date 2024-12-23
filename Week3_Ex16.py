"""
7. Nhập 2 từ điển A có N cặp (key, value) và B có M cặp (key, value).
Từ A và B hãy tạo từ điển C theo quy tắc sau:
• Một mục trong C thì key phải xuất hiện trong A hoặc B
• Nếu key chỉ xuất hiện trong A hoặc trong B thì value là value
tương ứng trong A (hoặc B)
• Nếu key xuất hiện trong cả A và B thì value là max của value tương ứng trong A và B
"""
A = {'a': 1, 'b': 3, 'c': 5, 'd': 9}
B = {'b': 4, 'd': 2, 'e': 7, 'g': 5, 'j': 12}
C = {}

for key in A.keys():
    if key in B:
        C[key] = max(A[key], B[key])
    else:
        C[key] = A[key]

for key in B.keys():
    if key not in A:
        C[key] = B[key]
print(C)

