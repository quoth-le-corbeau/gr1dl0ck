from converters import (
    hex_to_b64,
    b64_to_hex,
    custom_hex_to_b64,
    custom_hex_to_binary,
    _bin_to_base_10,
    custom_b64_to_hex,
    custom_hex,
    custom_bin,
)
from test.reuseables import dict_parametrize

TEST_HEX = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
TEST_B64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
HELLO_HEX = "48656c6c6f"
HELLO_B64 = "SGVsbG8="


@dict_parametrize(
    {
        "case_1": {"hex_string": TEST_HEX, "expected_base64_converted": TEST_B64},
        "hello": {"hex_string": HELLO_HEX, "expected_base64_converted": HELLO_B64},
    }
)
def test_hex_to_b64(hex_string, expected_base64_converted):
    assert hex_to_b64(hex=hex_string) == expected_base64_converted


@dict_parametrize(
    {
        "case_1": {"base64_string": TEST_B64, "expected_hex_converted": TEST_HEX},
        "hello": {"base64_string": HELLO_B64, "expected_hex_converted": HELLO_HEX},
    }
)
def test_b64_to_hex(base64_string, expected_hex_converted):
    assert b64_to_hex(b64=base64_string) == expected_hex_converted


@dict_parametrize(
    {
        "case_1": {"hex_string": TEST_HEX, "expected_base64_converted": TEST_B64},
        "Hello": {"hex_string": HELLO_HEX, "expected_base64_converted": HELLO_B64},
    }
)
def test_custom_hex_to_b64(hex_string, expected_base64_converted):
    assert custom_hex_to_b64(hex_string=hex_string) == expected_base64_converted


@dict_parametrize(
    {
        "case_1": {"b64_string": TEST_B64, "expected_hex_converted": TEST_HEX},
        "Hello": {"b64_string": HELLO_B64, "expected_hex_converted": HELLO_HEX},
    }
)
def test_custom_b64_to_hex(b64_string, expected_hex_converted):
    assert custom_b64_to_hex(b64_string=b64_string) == expected_hex_converted


@dict_parametrize(
    {
        "case_1": {"n": 255, "expected_hex": "0xff"},
        "case_2": {"n": -255, "expected_hex": "-0xff"},
        "case_3": {"n": 0, "expected_hex": "0x0"},
        "case_4": {"n": 4096, "expected_hex": "0x1000"},
    }
)
def test_custom_hex(n, expected_hex):
    assert custom_hex(n=n) == expected_hex


@dict_parametrize(
    {
        "case_1": {"n": 10, "expected_bin": "0b1010"},
        "case_2": {"n": -10, "expected_bin": "-0b1010"},
        "case_3": {"n": 0, "expected_bin": "0b0"},
    }
)
def test_custom_bin(n, expected_bin):
    assert custom_bin(n=n) == expected_bin


@dict_parametrize(
    {
        "Hello": {
            "hex_string": HELLO_HEX,
            "expected_binary_values": [
                "01001000",
                "01100101",
                "01101100",
                "01101100",
                "01101111",
            ],
        },
        "case_1": {
            "hex_string": TEST_HEX,
            "expected_binary_values": [
                "01001001",
                "00100111",
                "01101101",
                "00100000",
                "01101011",
                "01101001",
                "01101100",
                "01101100",
                "01101001",
                "01101110",
                "01100111",
                "00100000",
                "01111001",
                "01101111",
                "01110101",
                "01110010",
                "00100000",
                "01100010",
                "01110010",
                "01100001",
                "01101001",
                "01101110",
                "00100000",
                "01101100",
                "01101001",
                "01101011",
                "01100101",
                "00100000",
                "01100001",
                "00100000",
                "01110000",
                "01101111",
                "01101001",
                "01110011",
                "01101111",
                "01101110",
                "01101111",
                "01110101",
                "01110011",
                "00100000",
                "01101101",
                "01110101",
                "01110011",
                "01101000",
                "01110010",
                "01101111",
                "01101111",
                "01101101",
            ],
        },
    }
)
def test_custom_hex_to_binary(hex_string, expected_binary_values):
    assert custom_hex_to_binary(hex_string=hex_string) == expected_binary_values


@dict_parametrize(
    {
        "eighteen": {"six_bit_chunk": "010010", "expected_base_10": 18},
    }
)
def test__bin_to_base_10(six_bit_chunk, expected_base_10):
    assert _bin_to_base_10(six_bit_chunk) == expected_base_10
