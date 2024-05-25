def e_bit_selection(input_32_bits):
    # Define the E-bit selection table
    e_table  = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
    # Initialize an empty output string
    output_48_bits = ""

    # Map input bits to output using the E-table
    for position in e_table:
        output_48_bits += input_32_bits[position - 1]  # Adjust for 0-based indexing

    return output_48_bits

# Example usage
input_bits = "0001100010101110001000001101101000111011111101110000010011010101"

  # Replace with your 32-bit input
output_bits = e_bit_selection(input_bits)
print("E-bit selection output (48 bits):", output_bits)