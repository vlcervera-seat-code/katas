import pytest
from expects import expect, equal
from typing import List
from main import RangeExtraction


@pytest.mark.parametrize(
    "input,output",
    [
        (
            [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15],
            "-10--8,-6,-3-1,3-5,7-11,14,15",
        ),
        (
            [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
            "-6,-3-1,3-5,7-11,14,15,17-20",
        ),
        (
            [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20],
            "-3--1,2,10,15,16,18-20",
        ),
    ],
)
class TestRangeExtraction:
    def test_extracts_a_range(self, input: List[int], output: str) -> None:
        range_extraction = RangeExtraction(input)
        expect(range_extraction.extract()).to(equal(output))
