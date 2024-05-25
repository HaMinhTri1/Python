a = "01100110000000000110011011111111"
b = "01100100011110001111001001011010"

# Convert binary strings to integers
int_a = int(a, 2)
int_b = int(b, 2)

# Perform XOR operation
result = int_a ^ int_b

# Convert result back to binary string
result_binary = '{0:b}'.format(result)

print(result_binary)
