from functions.user_inputs import parse_user_inputs, verify_numeric_inputs
import pytest


@pytest.mark.parametrize("inputs, expected", [
    (['func', 'test.csv', '5'], ['test.csv', 0, 5]),
    (['func'], ['error']),
    (['func', 'test.csv'], ['test.csv', 0, 0]),
    (['func', 'test.csv', '1', '2'], ['test.csv', 1, 2]),
])
def test_parse_user_input(inputs, expected):

    # Run the function
    if len(inputs) > 1:
        filename, results = parse_user_inputs(inputs)

        assert filename == expected[0]
        assert results == expected[1:]

    else:
        with pytest.raises(Exception):
            parse_user_inputs(inputs)


@pytest.mark.parametrize("inputs, expected", [
    ('test', False),
    ('1f2c', False),
    ('12', True),
    ('0.0023', True),
])
def test_verify_numeric_inputs(inputs, expected):

    # Run the function
    assert verify_numeric_inputs(inputs) == expected
