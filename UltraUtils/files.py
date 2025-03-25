def read_file(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def write_file(filepath: str, content: str) -> None:
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

def append_file(filepath: str, content: str) -> None:
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(content)

def file_exists(filepath: str) -> bool:
    import os
    return os.path.exists(filepath)

def delete_file(filepath: str) -> None:
    import os
    if os.path.exists(filepath):
        os.remove(filepath)

def count_lines(filepath: str) -> int:
    return len(read_file(filepath).splitlines())

def count_words(filepath: str) -> int:
    return len(read_file(filepath).split())

def get_file_size(filepath: str) -> int:
    import os
    return os.path.getsize(filepath) if file_exists(filepath) else 0

def copy_file(src: str, dest: str) -> None:
    import shutil
    shutil.copy(src, dest)

def move_file(src: str, dest: str) -> None:
    import shutil
    shutil.move(src, dest)

def list_files(directory: str) -> list:
    import os
    return os.listdir(directory)

def create_file(filepath: str) -> None:
    with open(filepath, "w") as file:
        pass
