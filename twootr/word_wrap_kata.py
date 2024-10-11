
class Wrapper:
    # Word wrap kata

    @staticmethod
    def wrap(string: str, max_column_num: int) -> str:
        """Wraps a string into multiple lines.

        Args:
            words (str): Initial string
            max_column_num (int): The maximum line length

        Returns:
            str: The string, but with line breaks inserted at just the right
            places to make sure that no line is longer than the column number.
        """
        line_start: int = 0
        line_end: int = line_start + max_column_num
        line: str = string[line_start:line_end]

        # Base cases
        # Max column number is zero
        if max_column_num == 0:
            return line
        # Line length is smaller than the provided max column number
        if len(line) < max_column_num:
            return line
        # Line is the last in string
        if len(line) == len(string):
            return line

        # Pre
        # Line end is not a word boundary
        if line[-1] != " " and line.rfind(" ") != -1:
            line_end = string[:line_end].rfind(" ") + 1

        # Recurse
        return string[:line_end] + "\n" + Wrapper.wrap(string[line_end:], max_column_num)


class TestWrapper:

    def test_wraps_empty_string(self):
        result = Wrapper.wrap("", 10)
        assert "" == result

    def test_should_do_nothing_with_zero_len(self):
        result = Wrapper.wrap("a", 0)
        assert "" == result

    def test_string_is_smaller_than_max_column_num(self):
        result = Wrapper.wrap("some string", 12)
        assert "some string" == result

    def test_string_is_longer_than_max_column_num(self):
        result = Wrapper.wrap("somelargeword", 10)
        assert "somelargew\nord" == result

    def test_string_is_longer_than_max_column_num_and_wraps_in_previous_word_boundary(self):
        result = Wrapper.wrap("some largeword", 10)
        assert "some \nlargeword" == result

    def test_string_is_equal_to_max_column_num(self):
        result = Wrapper.wrap("some string", 11)
        assert "some string" == result

    def test_string_should_be_wrapped_twice_in_end_previous_word_boundaries(self):
        result = Wrapper.wrap("this string should be wrapped twice", 15)
        assert "this string \nshould be \nwrapped twice" == result

    def test_string_should_be_wrapped_twice_after_word_boundaries(self):
        result = Wrapper.wrap("this string is wrapped. Twice", 12)
        assert "this string \nis wrapped. \nTwice" == result
