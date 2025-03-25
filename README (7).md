# UltraUtils  

[![UltraUtils](https://img.shields.io/badge/UltraUtils-v1.0.0-blue?style=flat-square)](https://github.com/ProgrammerKR/UltraUtils)
[![Python](https://img.shields.io/badge/Python-3.6+-brightgreen?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![ProgrammerKR](https://img.shields.io/badge/GitHub-ProgrammerKR-%23ADD8E6?style=flat-square&logo=github)](https://github.com/ProgrammerKR)

UltraUtils is a **lightweight and powerful Python utility library** that provides essential helper functions for:
- **String Manipulation**
- **File Handling**
- **Math Operations**
- **Date & Time Utilities**
- **List Processing**
- **Dictionary Utilities**
- **Random Generators**
- **System Utilities**

UltraUtils makes **Python development faster** and **more efficient** with reusable and well-optimized functions.

---

## 🚀 **Installation**  
Install UltraUtils using pip:
```sh
pip install ultrautils
```

Or install from source:
```sh
git clone https://github.com/ProgrammerKR/UltraUtils.git
cd UltraUtils
pip install .
```

---

## 📌 **Usage Examples**

### 🔹 **String Utilities**
```python
from ultrautils import reverse_string, to_upper, is_palindrome

print(reverse_string("hello"))  # "olleh"
print(to_upper("hello"))        # "HELLO"
print(is_palindrome("madam"))   # True
```

### 🔹 **File Handling**
```python
from ultrautils import write_file, read_file

write_file("test.txt", "Hello, UltraUtils!")
print(read_file("test.txt"))  # "Hello, UltraUtils!"
```

### 🔹 **Math Operations**
```python
from ultrautils import add, multiply, is_prime

print(add(10, 5))       # 15
print(multiply(4, 3))   # 12
print(is_prime(7))      # True
```

### 🔹 **Date & Time Utilities**
```python
from ultrautils import get_current_datetime, get_weekday

print(get_current_datetime())  # 2025-03-25 10:30:45
print(get_weekday(get_current_datetime()))  # "Tuesday"
```

### 🔹 **List Processing**
```python
from ultrautils import remove_duplicates, sort_list

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]
print(sort_list([3, 1, 4, 2]))               # [1, 2, 3, 4]
```

### 🔹 **Dictionary Utilities**
```python
from ultrautils import merge_dicts, keys_list

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dicts(d1, d2))  # {"a": 1, "b": 3, "c": 4}
print(keys_list(d1))        # ["a", "b"]
```

### 🔹 **Random Generators**
```python
from ultrautils import random_int, random_string

print(random_int(1, 100))      # Random integer between 1-100
print(random_string(8))        # "Xk9AbcD2"
```

---

## 🔥 **Why Use UltraUtils?**
✅ **Lightweight & Fast** – No extra dependencies  
✅ **Optimized & Well-Structured** – Clean and reusable functions  
✅ **Improves Productivity** – Saves time on common tasks  
✅ **100% Open Source** – MIT licensed  

---

## ⚡ **Contributing**
Want to improve UltraUtils?  
1. **Fork the repository**  
2. **Create a new branch**  
3. **Make changes & test**  
4. **Submit a pull request**  

We appreciate your contributions! 🚀  

---

## 📜 **License**
UltraUtils is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

## 💡 **Connect with Me**
[![GitHub](https://img.shields.io/badge/GitHub-ProgrammerKR-%23ADD8E6?style=flat-square&logo=github)](https://github.com/ProgrammerKR)  
