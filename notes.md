# What Happens When You Run a Python Program?
**1. Running Python Programs:**

- When you run a Python script (a .py file), Python interprets your code. It doesn’t directly talk to your computer’s hardware like other programming languages do (e.g., C or C++). Instead, it takes your code and translates it into something it can understand internally.

**2. Bytecode:**

- Python doesn’t execute your original code directly. Instead, it first compiles your Python code into bytecode (a lower-level, more efficient version of your code).
- Bytecode is not machine code (which the hardware understands), but it’s Python-specific and is easier to run repeatedly.
- Normally, you don’t see this bytecode because it’s hidden, but when you import a Python file into another file, Python will create a folder called __pycache__. Inside this folder, Python stores the bytecode in a file with the extension .pyc.
 
**3. Python Virtual Machine (PVM):**

- Python uses something called the Python Virtual Machine (PVM), which is like a small computer program that reads the bytecode and executes it.
- This is why Python is known as an interpreted language — the PVM interprets the bytecode and runs it line by line.
- The PVM is what makes Python run the bytecode on your computer, and it is automatically installed when you download Python.

**4. .pyc Files:**

- A .pyc file is the compiled bytecode version of your Python code.
- These files are stored in the __pycache__ folder to help Python run your programs faster in the future, so it doesn’t have to recompile the code every time.

**5.CPython, Jython, etc.:**

- CPython is the standard implementation of Python. When you download Python from the official website, you are downloading CPython.
- Other versions like Jython (for Java), IronPython (for .NET), PyPy (faster version of Python) also exist, but they all work in a similar way — they translate Python code into some intermediate form (like bytecode) and then run it.

**6. Python is not machine code:**

- The bytecode created by Python is not machine code (it cannot run directly on the hardware). It still needs to be interpreted by the PVM (Python Virtual Machine).

<hr>
<hr>

# Memory representation
- always remmber that when we create a variable so our data stire in memory si firstly data store in memory and then assign any variabale. 
- all data type is store in memory. vo variable pa nh jata.
- we never say that this variable is int , string etc. 
- always we say the data that store in memory that you are the this data type and this variable refrence you.

<p>In python not any data type for varible but in memory the refrence have data type</p>


# 1. What is an Object?
<p > in Python, everything is an object. Whether it’s a simple integer, a list, or even a function, all data types are objects. This is one of the fundamental principles of Python: everything is an object.</p>

- When you create a variable, Python creates an object for that value in memory.

- a = 10    # 'a' is a reference to an integer object with the value 10
- b = "hi"  # 'b' is a reference to a string object with the value "hi"

# 2. What is a Reference?
<p>A reference is like a pointer or a label that points to the location in memory where the object exists. <br> - When you assign a value to a variable, <br>- that variable is not the object itself, <br>- it’s a reference to that object in memory.</p>

- x = 5  # 'x' is a reference to the object 5
- y = x  # 'y' is now also a reference to the same object 5

Here, both x and y are references that point to the same object 5 in memory.
<b>Key point:</b> The variables x and y don't "store" the value directly. They "point"() to the object that holds the value.

# 3. Metadata
metadata is "data about data." It's information that describes or provides more details about other data or objects.

If you have a book, the book itself contains the main data (the story or content). But there’s extra information about the book like:

- The title
- The author
- The publication date
- The number of pages

This extra information is the metadata for the book. It tells you important details about the book but is not part of the story itself.

**In the context of Python objects:**

When we say metadata of an object, we’re talking about details related to the object, like:

- Type of the object (e.g., integer, string, list)
- Size of the object (how much memory it takes up)
- Reference count (how many references point to this object)
- Attributes or methods that belong to the object (functions you can use with the object)

# Garbage collector

The garbage collector in Python is like a cleanup worker that automatically removes things (objects) from memory when they are no longer needed. This prevents your computer from running out of memory by making sure unused data is thrown away.

### **How it works:**
**Reference Counting:** Every object in Python keeps track of how many variables are using it (references). When no variable is using the object anymore (its reference count becomes zero), Python's garbage collector deletes it from memory.

**Cyclic Garbage Collection:** Sometimes, two or more objects point to each other in a loop (a cycle), and no other variable uses them. Python's garbage collector can detect these "cycles" and clean them up to

<hr>
<hr>



## 1. repr()
 – "Official" or Debug Representation
Purpose: The repr() function is used to give an official, unambiguous representation of an object, mainly for debugging purposes.

**Goal:** The idea is that when you call repr(), it shows a string that can ideally be used to recreate the object.

**When to use:** Use repr() when you want a precise or detailed representation of the object, often for debugging.
#### repr() output
print(repr(now))  # Output: datetime.datetime(2024, 10, 5, 12, 0, 0)
repr(now) gives you the detailed, official representation (you could recreate the datetime object from this).


## 2.str() 
– "Human-Friendly" or Informal Representation
Purpose: The str() function is used to give a user-friendly, readable representation of an object.

**Goal:** It’s designed to return a string that’s easy for humans to read.

**When to use:** Use str() when you want to display or print an object in a simple, user-friendly way.

**str(now)** and **print(now)** give you the simple, human-readable version.



<hr><hr>

### Dictionary
- we can acess value by get() method

*ex:* **chai_dic** = [ 'lemon' : 'khati' , 'gengared' : 'karvi']
print(chai_dic.get('lemon')) *#output: khati*


when we use *POP()* Method for dic so we need to pass key that we wnat to pop like
*EX :* chai_dic.pop('lemon) #khati
But we don't wnat to pass key so we use *POPITEM()* Method for pop the complete 1 item in last
  