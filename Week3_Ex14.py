"""
5. Nhập từ điển prices lưu trữ giá của các loại trái cây và
từ điển stock lưu trữ số lượng tồn của từng loại.
Sau đó hãy in ra thứ tự các loại trái cây còn trong cửa
hàng giảm dần theo tổng giá trị của từng loại.
Ví dụ:
Dữ liệu nhập vào cho ra từ điện như sau:
    prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
    stock = { "banana": 6, "orange": 32, "pear": 15}
Kết quả in ra thứ tự:
    orange 48
    pear 45
    banana 24
    apple 0
"""
# Dữ liệu đầu vào
prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = { "banana": 6, "orange": 32, "pear": 15}
total_value = {}
for fruit in prices:
    if fruit in stock:
        total_value[fruit] = prices[fruit] * stock[fruit]
    else:
        total_value[fruit] = 0
result = sorted(total_value.items(), key=lambda x: x[1], reverse=True)
for fruit, value in result:
    print(f"{fruit} {int(value)}")
