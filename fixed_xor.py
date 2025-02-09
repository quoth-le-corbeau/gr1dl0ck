from converters import custom_hex_to_binary


def get_fixed_xor(hex_1: str, hex_2: str) -> str:
    binary1 = "".join(custom_hex_to_binary(hex_1))
    binary2 = "".join(custom_hex_to_binary(hex_2))
    xor_result_binary = "".join(
        str(int(b1) ^ int(b2)) for b1, b2 in zip(binary1, binary2)
    )
    hex_result = "".join(
        hex(int(xor_result_binary[i : i + 8], 2))[2:].zfill(2)
        for i in range(0, len(xor_result_binary), 8)
    )
    return hex_result
