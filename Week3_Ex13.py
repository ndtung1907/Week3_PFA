"""
4. Nhập một string S, hãy tạo từ điển D trong đó key là
các chữ xuất hiện trong S còn value tương ứng là số
lần xuất hiện các chữ đó trong S
Ví dụ: S = "dai hoc thuy loi"
       D= { 'd':1, 'a':1, 'i':2, '':3, 'h':2, 'o':2, 'c':1, 't':1, 'u':1, 'y':1, 'l':1}
"""
S = input("Nhập vào 1 chuỗi: ")
D = {}
for char in S:
    if char in D:
        D[char] += 1
    else:
        D[char] = 1
print(D)
