"""
6. Tạo ra một từ điển lưu lượng mưa trung bình trong các tháng từ năm 2000 đến 2019.
Quy cách như sau:
• Từ điển có 12 mục, khóa của mỗi mục là một tháng
• Giá trị ứng với khóa là danh sách 20 số đại diện cho 20 năm
• Lượng mưa là số thực ngẫu nhiên từ 100 đến 4000
"""
import random
result = {month: [random.uniform(100, 4000) for _ in range(20)] for month in range(1, 13)}
print(result)
