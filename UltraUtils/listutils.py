def flatten_list(lst): return [item for sublist in lst for item in sublist]
def unique_elements(lst): return list(set(lst))
def sort_list(lst): return sorted(lst)
def reverse_list(lst): return lst[::-1]
def list_intersection(lst1, lst2): return list(set(lst1) & set(lst2))
def list_union(lst1, lst2): return list(set(lst1) | set(lst2))
def remove_duplicates(lst): return list(dict.fromkeys(lst))
def get_max(lst): return max(lst)
def get_min(lst): return min(lst)
def sum_list(lst): return sum(lst)
def product_list(lst): from math import prod; return prod(lst)
def chunk_list(lst, size): return [lst[i:i+size] for i in range(0, len(lst), size)]
