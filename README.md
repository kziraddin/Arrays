# Array Operations in Python

This project demonstrates how to perform basic fixed-size array operations in Python, such as inserting elements at the end, at the beginning, and at a specified index. It mimics low-level array behavior (like in C/C++) using pre-allocated lists.

---

## 📁 File Structure

- `array_ops.py`: Core logic for array operations.
- `test_array.py`: Unit tests written using Python's `unittest` framework.
- `README.md`: Documentation file (you’re reading it!).

---

## ⚙️ Features

- Insert a value at the **end** of the array
- Insert a value at the **beginning**
- Insert a value at a **specific index**
- Input validation for:
  - Index bounds
  - Capacity overflow
- Console-based user interaction (in `__main__` block)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Run the Program

```bash
python3 arrays-.py
```

#### You’ll be prompted to enter the maximum capacity of the array and then perform insertion operations via a simple menu.

## 🧪 Running Unit Tests

#### We use the built-in unittest module to test the core functionality.

```bash
python3 -m unittest test_array.py
```

## ✅ Example Test Output

```sql
INFO:root:
Cannot insert. Array is full.
...INFO:root:
Out of range.
..INFO:root:
Cannot insert. Array is full.
.
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```


## 🔍 Logging

To make tests cleaner, we use the logging module instead of print() for error messages like:

"Cannot insert. Array is full."

"Out of range."

This allows for better testing and redirection during unit tests.



## 📌 Future Work
 ➕ Add support for deletion at a given index.

 🔍 Add search functionality.

 📋 Add a method to print only valid (inserted) elements.

 🧮 Make it dynamically resizable (like Python lists).

 ✅ Add more comprehensive unit tests (e.g., edge cases, bulk inserts, deletes).

 🧾 Store log and error messages in a file using Python logging handlers.
 


## 🧪 Planned Tests

We plan to include more detailed unit tests for:

insertAtEnd(): Test capacity overflow, insert when partially filled.

insertAtBeginning(): Insert into empty and full arrays, shifting all elements.

insertAtIndex(): Insert at start, middle, end, and test for invalid indices and full array.


## 📬 Feedback
Feel free to open issues or submit pull requests if you'd like to contribute or suggest improvements!

## 🧑‍💻 Author
Ziraddin — LinkedIn • GitHub

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

Let me know if you'd like to include example code snippets, add screenshots, or include a GIF showing interaction with the menu.
