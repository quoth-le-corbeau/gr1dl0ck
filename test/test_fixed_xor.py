from fixed_xor import get_fixed_xor
from test.reuseables import dict_parametrize


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
    pass
