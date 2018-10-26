import pytest
import os
from functions.write_results import gen_save_filename, gen_outpath


@pytest.mark.parametrize("input_file, expected", [
    ('/results/results1.csv', 'output_data/results1.json'),
    ('\\test_folder\\names.csv', 'output_data/names.json'),
    ('mega/man_.tif', 'output_data/man_.json'),
])
def test_gen_save_filename(input_file, expected):

    # Run the test
    result = gen_save_filename(input_file)

    assert result == expected


@pytest.mark.parametrize("input_str, expected", [
    ('/results/', 'results'),
    ('\\test_folder\\', 'test_folder'),
    ('mega/', 'mega'),
])
def test_gen_outpath(input_str, expected):

    # Generate folder
    gen_outpath(input_str)

    # Test that the folder exists
    assert os.path.exists(expected)

    # Remove test folders
    os.rmdir(expected)
