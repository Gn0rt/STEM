import re


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def process_string(s):
    # Bước 1: Tìm tất cả các chữ số trong chuỗi
    digits = re.findall(r'\d', s)
    joined_digits = ''.join(digits)
    print(f"Tổng số chữ số: {len(joined_digits)}")
    print(f"Chuỗi số liên tục: {joined_digits}")

    # Bước 2: Tìm các cụm số liên tiếp (vd: '000', '0101', '02', '7', '17')
    numbers = re.findall(r'\d+', s)
    prime_numbers = [int(num) for num in numbers if is_prime(int(num))]

    if prime_numbers:
        max_prime = max(prime_numbers)
        print(f"Số nguyên tố lớn nhất: {max_prime}")
    else:
        print("Không có số nguyên tố nào trong chuỗi.")


# Ví dụ
s = "asbdjhd000sdse0101rrw02dđ7dd17ddd"
process_string(s)
