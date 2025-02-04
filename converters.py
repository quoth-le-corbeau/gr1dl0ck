from base64 import b64encode, b64decode
import codecs

_BASE_2 = 2
_BASE_16 = 16
_BASE_64_BINARY_CHUNK_LENGTH = 6
_BASE_64_STRING_LENGTH_DIVISOR = 4


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
    base64_look_up_string = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    )
    binary_string: str = "".join(_hex_to_binary(hex_string))
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
        base64_look_up_string[decimal_value] for decimal_value in decimal_values
    )
    if len(base64_encoded_string) % _BASE_64_STRING_LENGTH_DIVISOR != 0:
        padding = _BASE_64_STRING_LENGTH_DIVISOR - (
            len(base64_encoded_string) % _BASE_64_STRING_LENGTH_DIVISOR
        )
        base64_encoded_string += "=" * padding
    return base64_encoded_string


def _hex_to_binary(hex_string: str) -> list[str]:
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
