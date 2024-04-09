Nb = 4  # Số cột trong mỗi hàng của State
shift_values = [0, 3, 2, 1]  # Giá trị dịch chuyển cho từng hàng

def inv_shift_rows(state):
    for row in range(1, 4):  # Dịch chuyển từ hàng thứ 2 đến hàng thứ 4
        state[row] = invshift_row(state[row], row)
    return state

def invshift_row(row, shift_amount):
    return row[shift_amount:] + row[:shift_amount]

state = [
    [0, 1, 2, 3],
    [5, 6, 7, 4],
    [10, 11, 8, 9],
    [15, 12, 13, 14]
]

def invshift_row(row, shift_amount):
    return row[-shift_amount:] + row[:-shift_amount]

result = inv_shift_rows(state)
print(result)


