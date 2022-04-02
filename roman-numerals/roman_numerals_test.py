from roman_numerals import RomanNumerals
import pytest


class TestRomanNumerals:
    @pytest.mark.parametrize(
        "amount,roman",
        [
            (1, "I"),
            (5, "V"),
            (10, "X"),
            (50, "L"),
            (100, "C"),
            (500, "D"),
            (1000, "M"),
            (4, "IV"),
            (9, "IX"),
            (29, "XXIX"),
            (80, "LXXX"),
            (294, "CCXCIV"),
            (2019, "MMXIX"),
        ],
    )
    def test_transform_from_arabic_to_roman(self, amount, roman):
        assert RomanNumerals().calculate(amount) == roman
