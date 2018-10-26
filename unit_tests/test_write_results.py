import pytest
import os
import json
from functions.write_results import gen_save_filename, gen_outpath
from functions.write_results import write_json


@pytest.mark.parametrize("input_file, expected", [
    ('/results/results1.csv', 'output_data/results1.json'),
    ('\\test_folder\\names.csv', 'output_data/names.json'),
    ('mega/man_.tif', 'output_data/man_.json'),
])
def test_gen_save_filename(input_file, expected):

    # Run the test
    save_path = 'output_data'
    result = gen_save_filename(input_file, save_path)

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


@pytest.mark.parametrize("filename, expected", [
    ('happy.json', True),
    ('test.json', True),
    ('for/me.json', False)
])
def test_write_json(filename, expected):

    # Set up input data
    metrics = {'test': 'some text'}

    # Run code
    if filename == 'for/me.json':  # An exception for a nonexistent folder

        with pytest.raises(FileNotFoundError):
            write_json(metrics, filename)

    else:
        write_json(metrics, filename)

        # Check file existence
        assert os.path.exists(filename) == expected

        # Check the contents of the file
        with open(filename, 'r') as f:
            test = json.load(f)

        assert metrics['test'] == test['test']

        # Remove dummy file
        os.remove(filename)
