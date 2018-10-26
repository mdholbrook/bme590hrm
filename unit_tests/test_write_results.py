import pytest
from functions.write_results import gen_save_filename


@pytest.mark.parametrize("input_file, expected", [
    ('/results/results1.csv', 'output_data/results1.json'),
    ('\\test_folder\\names.csv', 'output_data/names.json'),
    ('mega/man_.tif', 'output_data/man_.json'),
])
def test_gen_save_filename(input_file, expected):

    # Run the test
    result = gen_save_filename(input_file)

    assert result == expected
