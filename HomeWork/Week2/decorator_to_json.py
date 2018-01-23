import functools
import json


def to_json(func):
    @functools.wraps(func)
    def inner(*args):
        val = func(*args)
        return json.dumps(val)
    return inner

