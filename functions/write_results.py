import json

def write_json(df, file_descriptor):

    filename = 'output_data/metrics_%s.json' %file_descriptor

    with open(filename, 'w') as fp:
        json.dump(df, fp)

