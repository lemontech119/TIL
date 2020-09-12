input_data = input()
row = ord(input_data[0])-96
column = input_data[1]

knight_row = [2, 2, -2, -2, 1, -1, 1, -1]
knight_column = [1, -1, 1, -1, 2, 2, -2, -2]

case = 0

for knight in range(8):
    case_row = row + knight_row[knight]
    case_column = row + knight_column[knight]
    if 1 <= case_row <= 8 and 1 <= case_column <= 8:
        case += 1

print(case)
