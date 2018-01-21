import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


parser = argparse.ArgumentParser()
parser.add_argument('--key', help='input key')
parser.add_argument('--val', help='input values')
args = parser.parse_args()

def read_temp_file():
    with open(storage_path, 'r') as f:
        temp_dict = json.dumps(f.read())
    return temp_dict

def write_temp_file(text):
    with open(storage_path, 'w') as f:
        f.write(json.loads(text))


print(read_temp_file())
'''
if args.val:
    temp_dict = read_temp_file()
    temp_dict.update({args.key: args.val})
    write_temp_file('{'+args.key+':'+args.val+'}')
else:
    print(read_temp_file()[args.key])
'''