def inv_mix_columns(state):
    # Define the inverse matrix a^-1(x) = 0x0e * x^3 + 0x0b * x^2 + 0x09 * x + 0x0d
    inv_a = [[0x0e, 0x0b, 0x0d, 0x09],
             [0x09, 0x0e, 0x0b, 0x0d],
             [0x0d, 0x09, 0x0e, 0x0b],
             [0x0b, 0x0d, 0x09, 0x0e]]

    # Create a new state matrix to store the result
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for i in range(4):  # for each column in the state
        for j in range(4):  # for each row in the state
            new_state[j][i] = (
                gf_mult(inv_a[j][0], state[0][i]) ^
                gf_mult(inv_a[j][1], state[1][i]) ^
                gf_mult(inv_a[j][2], state[2][i]) ^
                gf_mult(inv_a[j][3], state[3][i])
            )

    return new_state
def gf_mult(a, b):
    # Multiply two numbers in GF(2^8) modulo x^4 + 1
    result = 0
    for _ in range(8):
        if b & 1:  # If the least significant bit of b is set
            result ^= a  # Add a to the result
        a <<= 1  # Left shift a
        if a & 0x100:  # If a overflows past 8 bits
            a ^= 0x11B  # XOR with the irreducible polynomial x^8 + x^4 + x^3 + x + 1
        b >>= 1  # Right shift b
    return result
state = [[112, 144, 31, 138], [208, 40, 193, 69], [80, 207, 169, 69], [9, 67, 31, 207]]

new_state = inv_mix_columns(state)
for row in new_state:
    print([hex(val) for val in row])