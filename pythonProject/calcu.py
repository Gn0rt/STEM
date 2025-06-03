#chuẩn hóa
string = "    bUI tHe TrONg"

lists = string.split()
length = len(lists)
newSring = ""
for i in range(length):
    newSring += (lists[i].capitalize() + " ")

print(string.split())
print(newSring)