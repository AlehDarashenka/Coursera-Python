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
        temp_dict = json.loads(f.read())
    return temp_dict

def write_temp_file(text):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(text))


def get_value(diction, key):
    try:
        return diction[key]
    except KeyError:
        return None



def conn_warehouse(temp_dict):
    if args.val:
        vals = get_value(temp_dict,args.key)
        if vals:
            if isinstance(vals, list):
                if args.val not in vals:
                    vals.append(args.val)
                    temp_dict.update({args.key: vals})
            elif args.val != vals:
                temp_dict.update({args.key: [vals, args.val]})
        else:
            temp_dict.update({args.key: args.val})
        write_temp_file(temp_dict)
    elif args.key:
        response = get_value(temp_dict, args.key)
        if isinstance(response, list):
            print(', '.join(response))
        else:
            print(response)

try:
    temp_dict = read_temp_file()
    conn_warehouse(temp_dict)
except FileNotFoundError:
    if args.val:
        write_temp_file({args.key: args.val})
    elif args.key:
        print(None)





