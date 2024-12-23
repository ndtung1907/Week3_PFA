"""
3. Nhập một từ điển D có các value là các số nguyên, hãy in ra màn hình 3 giá trị value lớn nhất.
"""
D = eval(input("Nhập vào 1 từ điển có các value là các số nguyên: "))

result = sorted(set(D.values()), reverse=True)[:3]
print(result)