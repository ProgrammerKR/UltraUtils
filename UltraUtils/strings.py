def reverse_string(s: str) -> str:
    return s[::-1]

def to_upper(s: str) -> str:
    return s.upper()

def to_lower(s: str) -> str:
    return s.lower()

def capitalize_string(s: str) -> str:
    return s.capitalize()

def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def remove_spaces(s: str) -> str:
    return s.replace(" ", "")

def remove_digits(s: str) -> str:
    return ''.join(c for c in s if not c.isdigit())

def remove_punctuation(s: str) -> str:
    import string
    return ''.join(c for c in s if c not in string.punctuation)

def contains_substring(s: str, sub: str) -> bool:
    return sub in s

def word_count(s: str) -> int:
    return len(s.split())

def swap_case(s: str) -> str:
    return s.swapcase()
