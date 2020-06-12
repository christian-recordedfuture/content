from DateStringToISOFormat import parse_datestring_to_iso
import pytest


# date_value, day_first, year_first, fuzzy, expected_output
testdata = [
    ('05-11-2929', True, True, True, '2929-11-05T00:00:00'),
    ('05-11-2929', True, False, True, '2929-11-05T00:00:00'),
    ('05-11-2929', True, True, False, '2929-11-05T00:00:00'),
    ('05-11-2929', True, False, False, '2929-11-05T00:00:00'),
    ('05-11-2929', False, True, True, '2929-05-11T00:00:00'),
    ('05-11-2929', False, False, True, '2929-05-11T00:00:00'),
    ('05-11-2929', False, False, False, '2929-05-11T00:00:00'),
    ('2020-06-11T17:34:35.754203+03:00', True, True, True, '2020-11-06T17:34:35.754203+03:00'),
    ('2020-06-11T17:34:35.754203+03:00', True, False, True, '2020-11-06T17:34:35.754203+03:00'),
    ('2020-06-11T17:34:35.754203+03:00', True, True, False, '2020-11-06T17:34:35.754203+03:00'),
    ('2020-06-11T17:34:35.754203+03:00', True, False, False, '2020-11-06T17:34:35.754203+03:00'),
    ('2020-06-11T17:34:35.754203+03:00', False, True, True, '2020-06-11T17:34:35.754203+03:00'),
    ('2020-06-11T17:34:35.754203+03:00', False, False, True, '2020-06-11T17:34:35.754203+03:00'),
    ('2020-06-11T17:34:35.754203+03:00', False, False, False, '2020-06-11T17:34:35.754203+03:00')
]


@pytest.mark.parametrize('date_value,day_first,year_first,fuzzy,expected_output', testdata)
def test_parse_datestring_to_iso(date_value, day_first, year_first, fuzzy, expected_output):
    '''Scenario: Parse an arbitrary date string and convert it to ISO 8601 format

    Given
    - An arbitrary date string
    When
    - The date string can be an ambiguous 3-integer date or already an iso-8601 formatted date string
    Then
    - Ensure the output date string is in iso-8601 format in all cases

    Args:
        date_value (str): A string containing a date stamp.
        day_first (bool): Whether to interpret the first value in an ambiguous 3-integer date
                          (e.g. 01/05/09) as the day or month.
        year_first (bool): Whether to interpret the first value in an ambiguous 3-integer date
                           (e.g. 01/05/09) as the year. If ``True``, the first number is taken to
                           be the year, otherwise the last number is taken to be the year.
        fuzzy (bool): Whether to allow fuzzy parsing, allowing for string like "Today is
                      January 1, 2047 at 8:21:00AM".
        expected_output (str): The iso 8601 formatted date to check the result against
    '''
    assert parse_datestring_to_iso(date_value, day_first, year_first, fuzzy) == expected_output
