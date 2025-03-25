def merge_dicts(d1, d2): return {**d1, **d2}
def keys_list(d): return list(d.keys())
def values_list(d): return list(d.values())
def invert_dict(d): return {v: k for k, v in d.items()}
def remove_key(d, key): d.pop(key, None)
def filter_dict(d, keys): return {k: d[k] for k in keys if k in d}
def dict_size(d): return len(d)
def get_key(d, value): return [k for k, v in d.items() if v == value]
def clear_dict(d): d.clear()
def update_dict(d, key, value): d[key] = value
def key_exists(d, key): return key in d
def value_exists(d, value): return value in d.values()
