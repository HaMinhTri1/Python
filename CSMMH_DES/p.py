def e_bit_selection(input_32_bits):
    # Define the E-bit selection table
    e_table  = [16,  7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2,  8, 24, 14,
       32, 27,  3,  9,
       19, 13, 30,  6,
       22, 11,  4, 25]

    # Initialize an empty output string
    output_48_bits = ""

    # Map input bits to output using the E-table
    for position in e_table:
        output_48_bits += input_32_bits[position - 1]  # Adjust for 0-based indexing

    return output_48_bits

# Example usage
input_bits = "0110011000000000011001101111111110000111010101011000011101010101"

  # Replace with your 32-bit input
output_bits = e_bit_selection(input_bits)
print("E-bit selection output (48 bits):", output_bits)