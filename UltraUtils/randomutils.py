import random
import string
import uuid

def random_int(a: int, b: int) -> int:
    """Returns a random integer between a and b (inclusive)."""
    return random.randint(a, b)

def random_float(a: float = 0.0, b: float = 1.0) -> float:
    """Returns a random float between a and b."""
    return random.uniform(a, b)

def random_choice(seq):
    """Returns a random element from a sequence."""
    return random.choice(seq)

def shuffle_list(lst: list) -> list:
    """Shuffles a list in place and returns it."""
    random.shuffle(lst)
    return lst

def generate_uuid() -> str:
    """Generates a random UUID (unique identifier)."""
    return str(uuid.uuid4())

def random_string(length: int = 8) -> str:
    """Generates a random string of letters and digits of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_random_color() -> str:
    """Generates a random hexadecimal color code."""
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def weighted_choice(choices: list) -> any:
    """Chooses a random element from a list with assigned weights."""
    values, weights = zip(*choices)
    return random.choices(values, weights=weights)[0]

def random_password(length: int = 12) -> str:
    """Generates a random password with letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def random_bool() -> bool:
    """Returns a random boolean value (True or False)."""
    return random.choice([True, False])

def random_date(start_year: int = 2000, end_year: int = 2030) -> str:
    """Generates a random date in YYYY-MM-DD format."""
    from datetime import datetime, timedelta
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def random_ip() -> str:
    """Generates a random IPv4 address."""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))
