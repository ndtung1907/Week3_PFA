"""
1. Cho D là từ điển định nghĩa cách đọc các chữ số ở tiếng Anh,
hãy in ra các value của D theo thứ tự tăng dần.
"""
D = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

result = [D[key] for key in sorted(D.keys())]
print(result)
