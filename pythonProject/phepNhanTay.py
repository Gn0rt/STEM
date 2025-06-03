from itertools import product
import math
def bai_1():
    inp = input("Nhập số nguyên N: ")
    N = int(inp)
    abs_N = abs(N)
    #Chúng ta cần tìm giá trị nhỏ nhất của |a - b|, nên ban đầu giả sử min_c là "rất lớn",
    #để khi gặp giá trị thực tế nhỏ hơn thì cập nhật lại.
    min_c = 1000000000000
    for i in range(1, int(math.isqrt(abs_N)) + 1):
        if abs_N % i == 0:
            j = abs_N // i

            if N > 0:
                c1 = abs(i - j)
                min_c = min(min_c, c1)
            # Với N < 0: a, b khác dấu (1 âm, 1 dương)
            else:
                c2 = abs(i + j)
                min_c = min(min_c, c2)

    print(min_c)
def bai_2():
    # Nhập dữ liệu
    n = int(input())                          # Dòng 1: độ dài dãy
    t = int(input())                          # Dòng 2: thứ tự cần tìm
    query_seq = list(map(int, input().split()))  # Dòng 3: dãy truy vấn
    tat_ca_day = product(range(1,n+1), repeat=n)


    def loc_day():
        day_so = []
        for day in tat_ca_day:
            hop_le = True
            for i in range(n):
                for j in range (i+1, n):
                    for k in range(j+1, n):
                        a = day[i]
                        b = day[j]
                        c = day[k]
                        #sắp xếp a,b cạnh nhỏ và c lớn
                        canh = sorted([a,b,c])
                        if canh[0] + canh[1] <= canh[2]:
                            hop_le = False
                            break
                    if not hop_le:
                        break
                if not hop_le:
                    break
            if hop_le:
                day_so.append(day)
        return day_so

    day_hop_le = loc_day()
    day_hop_le.sort()
    print("---------")
    # In từng phần tử của tat_ca_day
    for day in day_hop_le:
        print(day)
    print("---------")
    print(len(day_hop_le))
    thu_t = day_hop_le[t-1]
    print(thu_t)
    print(f"query_seq: {query_seq}")
    query_tuple = tuple(query_seq)
    print(f"query_tuple: {query_tuple}")
    thu_tu = day_hop_le.index(query_tuple) + 1
    print(thu_tu)
def bai_3():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    tong = 0

    mod = 10 ** 9 + 7

    for i in range(n):
        for j in range(i + 1, n):
            x = c[i] + c[j]

            hieu_a = abs(a[i] - a[j])
            hieu_b = abs(b[i] - b[j])

            y = hieu_a
            if hieu_b < hieu_a:
                y = hieu_b

            # Tính năng lực tổng hợp T(i, j) = X(i, j) * Y(i, j)
            t = x * y

            tong = (tong + t) % mod

    print(tong)
def bai_4():
    N,Q = map(int, input().split())
    a = list(map(int, input().split()))
    #danh sách lưu số kẹo, ban đầu số kẹo là 0
    keo = [0] * N
    for _ in range(Q):
        l,r,x,v = map(int, input().split())
        for i in range(l-1, r):
            print(f"Học sinh thứ {i+1} có mã {a[i]}")
            if a[i] % x == 0:
                keo[i] += v
                print(f"|Số kẹo của học sinh vị trí {i} có mã {a[i]} là: {keo[i]}|")
    print(keo)


while True:
    print("\n--- Menu ---")
    print("1. Bài 1: Tìm bộ số")
    print("2. Bài 2: Dãy TriSeq")
    print("3. Bài 3: Lớp học")
    print("4. Bài 4: Chia kẹo")
    print("0. Exit")

    choice = input("Mời bạn chọn: ")

    if choice == '1':
        bai_1()
    elif choice == '2':
        bai_2()
    elif choice == '3':
        bai_3()
    elif choice == '4':
        bai_4()
    elif choice == '0':
        print("Bạn đã thoát! Hẹn gặp lại ^^")
        break;
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại hoặc nhấn 0 để thoát.")


