from typing import List


class RangeExtraction:
    def __init__(self, input: List[int]):
        self.input = input
        self.ranges: List[str] = []

    def extract(self) -> str:
        current_range: List[int] = []
        for index, number in enumerate(self.input):
            if len(current_range) == 0:  # First element or after starting a new range
                current_range = [number]
            if index == len(self.input) - 1:  # Last element
                self._add_range(current_range)
                break
            if number + 1 != self.input[index + 1]:  # Next element is not consecutive
                self._add_range(current_range)
                current_range = [self.input[index + 1]]
            else:  # Next number is consecutive
                current_range.append(number + 1)
        return self._generate_extraction()

    def _add_range(self, range_list: List[int]) -> None:
        first = range_list[0]
        last = range_list[-1]
        if len(range_list) == 1:
            self.ranges.append(str(first))
        else:
            separator = self._separator(range_list)
            self.ranges.append(f"{first}{separator}{last}")

    @staticmethod
    def _separator(range_list: List[int]) -> str:
        return "-" if len(range_list) > 2 else ","

    def _generate_extraction(self) -> str:
        return ",".join(self.ranges)
