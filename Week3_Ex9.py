"""
9. Một công ty có 3 phòng chức năng có dùng thế dùng chung nhân viên là phòng nhân sự,
phòng hành chính và phòng truyền thông. Các nhân viên có mã nhân viên là các số nguyên dương.
Hãy thực hiện các việc:
a. Nhập danh sách mã nhân viên của cả 3 phòng, danh sách được viết liên tục trên một dòng, ngăn cách bởi dấu phẩy
b. Ba phòng ban này sử dụng bao nhiêu nhân viên?
c. In ra danh sách các mã nhân viên thuộc cả 3 phòng
d . In ra danh sách các mã nhân viên chỉ thuộc 1 phòng
e. Tìm cặp phòng dùng chung nhiều nhân viên nhất, nếu có nhiều cặp phòng như vậy thì in ra tất cả các cặp
f. Với từng phòng, in ra mã nhân viên đầu tiên của phòng (có mã nhỏ nhất)
"""

hr = set(map(int, input("Nhập danh sách mã nhân viên phòng nhân sự (ngăn cách bởi dấu phẩy): ").split(", ")))
admin = set(map(int, input("Nhập danh sách mã nhân viên phòng hành chính (ngăn cách bởi dấu phẩy): ").split(", ")))
media = set(map(int, input("Nhập danh sách mã nhân viên phòng truyền thông (ngăn cách bởi dấu phẩy): ").split(", ")))

all_employees = hr | admin | media  # Tập hợp tất cả nhân viên từ 3 phòng
print(f"Ba phòng ban sử dụng {len(all_employees)} nhân viên.")

common_to_all = hr & admin & media
print(f"Các mã nhân viên thuộc cả 3 phòng: {sorted(common_to_all)}")

only_in_one = (hr - (admin | media)) | (admin - (hr | media)) | (media - (hr | admin))
print(f"Các mã nhân viên chỉ thuộc 1 phòng: {sorted(only_in_one)}")

common_hr_admin = len(hr & admin)
common_hr_media = len(hr & media)
common_admin_media = len(admin & media)

max_common = max(common_hr_admin, common_hr_media, common_admin_media)

print("Cặp phòng dùng chung nhiều nhân viên nhất:")
if common_hr_admin == max_common:
    print("Phòng nhân sự và phòng hành chính")
if common_hr_media == max_common:
    print("Phòng nhân sự và phòng truyền thông")
if common_admin_media == max_common:
    print("Phòng hành chính và phòng truyền thông")

print(f"Mã nhân viên đầu tiên của phòng nhân sự: {min(hr)}")
print(f"Mã nhân viên đầu tiên của phòng hành chính: {min(admin)}")
print(f"Mã nhân viên đầu tiên của phòng truyền thông: {min(media)}")
