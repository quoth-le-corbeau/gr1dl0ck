from base64 import b64encode, b64decode
import codecs

_BASE_2 = 2
_BASE_16 = 16
_BASE_64_BINARY_CHUNK_LENGTH = 6
_BASE_64_STRING_LENGTH_DIVISOR = 4
_BYTE_LENGTH = 8
_BASE64_LOOK_UP_STRING = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
)


def hex_to_b64(hex: str) -> str:
    b64 = b64encode(bytes.fromhex(hex)).decode()
    b64_codecs = (
        codecs.encode(codecs.decode(hex, encoding="hex"), encoding="base64")
        .decode()
        .strip()
    )
    assert b64_codecs == b64
    return b64


def b64_to_hex(b64: str) -> str:
    return b64decode(b64.encode()).hex()


def custom_hex_to_b64(hex_string: str) -> str:
    """
    step 0:  Define the Base64 alphabet: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    step 1: convert hex to 8-bit binary values
    step 2: group into 6-bit chunks, if not a multiple of 6, add zero-padding at the end.
    step 3: convert each 6-bit chunk to its decimal value
    step 4: map each decimal value to the corresponding base64 value
    step 5: if necessary, add "=" padding to make the output length a multiple of 4.


    :param hex_string: a hexadecimal string
    :return: a base64 encoded string
    """

    binary_string: str = "".join(custom_hex_to_binary(hex_string))
    chunk_6 = [binary_string[i : i + 6] for i in range(0, len(binary_string), 6)]
    padded_chunk_6 = []
    for chunk in chunk_6:
        if len(chunk) != _BASE_64_BINARY_CHUNK_LENGTH:
            padding = _BASE_64_BINARY_CHUNK_LENGTH - len(chunk)
            padded_chunk = chunk + padding * "0"
            padded_chunk_6.append(padded_chunk)
        else:
            padded_chunk_6.append(chunk)
    decimal_values: list[int] = [_bin_to_base_10(chunk) for chunk in padded_chunk_6]
    base64_encoded_string = "".join(
        _BASE64_LOOK_UP_STRING[decimal_value] for decimal_value in decimal_values
    )
    if len(base64_encoded_string) % _BASE_64_STRING_LENGTH_DIVISOR != 0:
        padding = _BASE_64_STRING_LENGTH_DIVISOR - (
            len(base64_encoded_string) % _BASE_64_STRING_LENGTH_DIVISOR
        )
        base64_encoded_string += "=" * padding
    return base64_encoded_string


def custom_hex_to_binary(hex_string: str) -> list[str]:
    pairs = [hex_string[i] + hex_string[i + 1] for i in range(0, len(hex_string), 2)]
    hex_look_up_string = "0123456789ABCDEF"
    binary_values = []
    for pair in pairs:
        p1, p2 = hex_look_up_string.index(pair[0].upper()), hex_look_up_string.index(
            pair[1].upper()
        )
        base_10 = p1 * _BASE_16 + p2
        base_2 = bin(base_10)[2:].zfill(8)
        binary_values.append(base_2)
    return binary_values


def _bin_to_base_10(six_bit_chunk: str) -> int:
    total = 0
    for i, char in enumerate(six_bit_chunk[::-1]):
        total += int(char) * (_BASE_2**i)
    return total


def custom_b64_to_hex(b64_string: str) -> str:
    """
    step_0: remove b64 padding
    step_1: group data into 6-bit chunks.
        Note: you get a string that may not be a perfect multiple of 8 bits!
    step_2: group binary string into 8-bit segments.
        Note: If the binary string is padded, can lead to unnecessary trailing zeroes when converted to hex.
    step_3: trim excess bits that are not full byte (8-bits)

    :param b64_string:
    :return: converted to hex string
    """
    b64_string = b64_string.rstrip("=")
    binary_string = "".join(
        bin(_BASE64_LOOK_UP_STRING.index(c))[2:].zfill(_BASE_64_BINARY_CHUNK_LENGTH)
        for c in b64_string
    )
    excess_bits = len(binary_string) % _BYTE_LENGTH
    if excess_bits:
        binary_string = binary_string[:-excess_bits]
    hex_string = "".join(
        custom_hex(int(binary_string[i : i + _BYTE_LENGTH], 2))[2:].zfill(2)
        for i in range(0, len(binary_string), _BYTE_LENGTH)
    )
    return hex_string


def custom_hex(n: int) -> str:
    """
    Convert an integer to a hexadecimal string (mimicking Python's built-in hex() function).

    Steps:
    step_0: Handle edge case where n is 0 (return '0x0').
    step_1: Determine if the number is negative.
    step_2: Convert the absolute value of the number to hexadecimal.
    step_3: If negative, prepend '-0x', otherwise prepend '0x'.

    :param n: Integer to be converted to hex.
    :return: Hexadecimal string representation.
    """
    if n == 0:
        return "0x0"
    hex_chars = "0123456789abcdef"
    is_negative = n < 0
    n = abs(n)
    hex_result = ""
    while n > 0:
        remainder = n % _BASE_16
        hex_result = hex_chars[remainder] + hex_result
        n //= _BASE_16
    return "-0x" + hex_result if is_negative else "0x" + hex_result


def custom_bin(n):
    """
    Convert an integer to its binary representation as a string.

    Algorithm:
    step_0: Handle the special case where n is 0, returning '0b0'.
    step_1: If n is negative, convert its absolute value to binary and prepend '-0b'.
    step_2: Use repeated division by 2 to obtain the binary representation:
       - Initialize an empty list to store binary digits.
       - Use a loop to divide n by 2, storing the remainder each time.
       - Append remainders to the list, which will represent binary digits.
       - Reverse the list to get the correct order.
    step_3: Join the binary digits into a string and prepend '0b' to indicate binary format.
    step_4: Return the final binary representation.

    :param n: An integer to be converted to binary.
    :return: A string representing the binary format of the input integer.
    """
    if n == 0:
        return "0b0"

    is_negative = n < 0
    n = abs(n)
    reversed_binary_digits = []

    while n > 0:
        remainder = n % _BASE_2
        reversed_binary_digits.append(str(remainder))
        n //= _BASE_2

    binary_digits = reversed_binary_digits[::-1]
    binary_representation = "0b" + "".join(binary_digits)

    return "-" + binary_representation if is_negative else binary_representation
