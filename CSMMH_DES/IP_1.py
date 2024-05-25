def e_bit_selection(input_32_bits):
    # Define the E-bit selection table
    e_table  =[40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

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