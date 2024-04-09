def InvCipher(in_bytes, w):
    Nb = 4
    Nr = 10  # Assuming AES-128
    state = [in_bytes[i:i+Nb] for i in range(0, len(in_bytes), Nb)]
    
    state = AddRoundKey(state, w[Nr*Nb:(Nr+1)*Nb])  # Initial AddRoundKey
    
    for round in range(Nr-1, 0, -1):
        InvShiftRows(state)
        InvSubBytes(state)
        AddRoundKey(state, w[round*Nb:(round+1)*Nb])
        InvMixColumns(state)
    
    InvShiftRows(state)
    InvSubBytes(state)
    AddRoundKey(state, w[0:Nb])
    
    out_bytes = [byte for row in state for byte in row]
    
    return out_bytes

# Implement the required functions: InvShiftRows, InvSubBytes, InvMixColumns, AddRoundKey
# Define the AddRoundKey, InvShiftRows, InvSubBytes, InvMixColumns functions

# Example usage:
# out = InvCipher(in_bytes, w)
def InvSubBytes(state):
    pass  # Implement the Inverse SubBytes operation

def InvShiftRows(state):
    pass  # Implement the Inverse ShiftRows operation

def InvMixColumns(state):
    pass  # Implement the Inverse MixColumns operation

def AddRoundKey(state, key):
    pass  # Implement the AddRoundKey operation

