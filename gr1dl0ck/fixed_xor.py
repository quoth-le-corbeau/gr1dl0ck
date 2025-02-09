from gr1dl0ck.converters import custom_hex_to_binary, custom_hex


def get_fixed_xor(hex_1: str, hex_2: str) -> str:
    binary1 = "".join(custom_hex_to_binary(hex_1))
    binary2 = "".join(custom_hex_to_binary(hex_2))
    xor_result_binary = "".join(
        str(_custom_xor(int(b1), int(b2))) for b1, b2 in zip(binary1, binary2)
    )
    hex_result = "".join(
        custom_hex(int(xor_result_binary[i : i + 8], 2))[2:].zfill(2)
        for i in range(0, len(xor_result_binary), 8)
    )
    return hex_result


def _custom_xor(a: int, b: int) -> int:
    """
    Perform a bitwise XOR operation without using the ^ operator.

    step_0: iterate bit by bit using bitwise operations.
    step_1: extract the bits of `a` and `b` using the AND (`&`) and OR (`|`) operators.
    step_2: compute XOR for each bit using the formula: (a OR b) & ~(a AND b)
       - `a | b` ensures that if either bit is 1, the result is 1.
       - `a & b` ensures that only positions where both bits are 1 are marked.
       - `~(a & b)` flips these positions to 0, ensuring 1 ⊕ 1 = 0.
       - the final bitwise AND `&` gives us the XOR result.
    step_3: continue iteratively for all bit positions in `a` and `b`.

    Time Complexity: O(log n), where n is the number of bits in the largest number.

    Parameters:
    - a (int): First integer.
    - b (int): Second integer.

    Returns:
    - int: Result of `a XOR b`.

    """
    result = 0
    position = 1

    while a != 0 or b != 0:
        bit_a = a & 1
        bit_b = b & 1
        xor_bit = (bit_a | bit_b) & ~(bit_a & bit_b)
        result |= xor_bit * position
        a >>= 1
        b >>= 1
        position <<= 1
    return result
