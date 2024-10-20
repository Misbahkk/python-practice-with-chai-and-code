# **Understanding the Basics of Decorators**
- A decorator is a function that wraps another function and allows us to add functionality before or after the wrapped function is called, without modifying the function itself.
- Decorators are useful for logging, enforcing access control, instrumentation, timing, and mor

# How to Create a Simple Decorator
Let’s create a simple decorator that adds some functionality, such as printing a message before and after the function is called:

    `def my_decorator(func):`
        `def wrapper():`
            print("Before the function call.")
            func()  # Call the original function
            print("After the function call.")
        return wrapper

    `@my_decorator`
    `def say_hello():`
        print("Hello!")

    say_hello()

### **Output**
    Before the function call.
    Hello!
    After the function call.

Here’s what’s happening:

- The my_decorator function takes the say_hello function as input (via func).
- Inside my_decorator, a wrapper function is defined, which adds behavior before and after calling func().
- The say_hello() function is replaced by the wrapper() function when decorated, so when you call say_hello(), it actually calls the wrapper().



    
`

    def login_required(func):
        def wrapper(user, *args, **kwargs):
            if user['logged_in']:
                return func(*args, **kwargs)
            else:
                print("User is not logged in!")
        return wrapper

    @login_required
    def view_dashboard():
        print("Welcome to your dashboard!")

    user1 = {'logged_in': True}
    user2 = {'logged_in': False}

    view_dashboard(user1)  # Outputs: Welcome to your   dashboard!
    view_dashboard(user2)  # Outputs: User is not   logged in!