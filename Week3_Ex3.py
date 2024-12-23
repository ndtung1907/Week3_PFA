"""
3. Tạo một tập hợp gồm các số nhập vào từ bàn phím (nhập trên 1 dòng,
cách nhau bởi ký tự trồng), tìm và in ra số phần tử của tập, giá trị
lớn nhất và nhỏ nhất trong tập
"""
_input = set(map(int, input().split()))
print("Số phần tử:",len(_input))
print("Giá trị lớn nhất:",max(_input))
print("Giá trị nhỏ nhất:",min(_input))