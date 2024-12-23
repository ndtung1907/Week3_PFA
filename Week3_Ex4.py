"""
4. Nhập vào từ bàn phím họ và tên đầy đủ của các sinh viên trong lớp, mỗi người trên một dòng.
Việc nhập sẽ kết thúc khi người dùng gõ vào dòng trống. Sau đó, hãy in ra các họ và các tên của sinh viên trong lớp
"""
names = []
while True:
    full_name = input("Nhập đầy đủ họ và tên: ")

    if full_name == "":
        break
    names.append(full_name)
for student in names:
    name_parts = student.split()
    last_name = name_parts[0]
    fisrt_name = " ".join(name_parts[1:])
    print(f"Họ: {last_name}, Tên: {fisrt_name}")