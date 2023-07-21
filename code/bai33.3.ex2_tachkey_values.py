dict_01 = {
"A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
"H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
"O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
"V":4,"W":4,"X":8,"Y":4,"Z":10
}

dict_01 = {"A": 1, "B": 2, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

# Tách số và chữ trong dict và hiển thị lên màn hình
for key, value in dict_01.items():
    print(key, ":", value)

# Tính tổng các số trong dict
total = sum(dict_01.values())
print("Tổng các số trong dict là:", total)

# Chuyển đổi chuỗi "University of Technology and Education" sang số
string = "University of Technology and Education"
string = string.upper()  # Chuyển chuỗi thành chữ in hoa để so sánh với dict_01
result = []
for char in string:
    if char in dict_01:
        result.append(str(dict_01[char]))  # Chuyển giá trị của chữ sang kiểu string và lưu vào result
    else:
        result.append(char)
result = "".join(result)  # Ghép các phần tử trong result thành một chuỗi
print("Chuyển đổi chuỗi thành số:", result)
