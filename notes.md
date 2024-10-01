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


