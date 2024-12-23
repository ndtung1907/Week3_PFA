"""
8. Vé Vietlott Mega là bộ 6 số chỉ từ 01 đến 45.
Người chơi sẽ thắng nếu chọn đúng ít nhất 5 trong 6 số, thứ tự không quan trọng.
Hãy viết chương trình nhập vào N bộ 6 số của N người,
sau đó nhập tiếp 6 số của giải đặc biệt và in ra các bộ số của người chơi thắng cuộc.
"""
N = int(input("Nhập số lượng người chơi: "))

players_numbers = []
for i in range(N):
    numbers = set(map(int, input(f"Nhập bộ số của người chơi {i+1} (6 số ngăn cách nhau bằng dấu cách): ").split()))
    players_numbers.append(numbers)

special_numbers = set(map(int, input("Nhập bộ số giải đặc biệt (6 số ngăn cách nhau bằng dấu cách): ").split()))

winners = []
for i, numbers in enumerate(players_numbers):
    match_count = len(numbers & special_numbers)
    if match_count >= 5:
        winners.append((i+1, numbers))
if winners:
    print("Các người chơi thắng cuộc:")
    for winner in winners:
        print(f"Người chơi {winner[0]} với bộ số {sorted(winner[1])}")
else:
    print("Không có người chơi nào thắng cuộc.")
