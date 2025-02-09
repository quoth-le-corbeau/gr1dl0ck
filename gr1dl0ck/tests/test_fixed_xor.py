from gr1dl0ck.fixed_xor import get_fixed_xor, _custom_xor
from gr1dl0ck.tests.reuseables import dict_parametrize


@dict_parametrize(
    {
        "case_1": {
            "input_1": "1c0111001f010100061a024b53535009181c",
            "input_2": "686974207468652062756c6c277320657965",
            "expected_output": "746865206b696420646f6e277420706c6179",
        }
    }
)
def test_get_fixed_xor(input_1, input_2, expected_output):
    assert get_fixed_xor(input_1, input_2) == expected_output


@dict_parametrize({"case_1": {"a": 5, "b": 3, "expected_output": 6}})
def test__custom_xor(a, b, expected_output):
    assert a ^ b == expected_output
    assert _custom_xor(a, b) == expected_output
