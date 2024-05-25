def e_bit_selection(input_32_bits):
    # Define the E-bit selection table
    e_table = [
        32,  1,  2,  3,  4,  5,
         4,  5,  6,  7,  8,  9,
         8,  9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32,  1
    ]

    # Initialize an empty output string
    output_48_bits = ""

    # Map input bits to output using the E-table
    for position in e_table:
        output_48_bits += input_32_bits[position - 1]  # Adjust for 0-based indexing

    return output_48_bits

# Example usage
input_bits = "10000111010101011000011101010101"  # Replace with your 32-bit input
output_bits = e_bit_selection(input_bits)
print("E-bit selection output (48 bits):", output_bits)
