def login_required(func):
    def wrapper(user,*args,**kwargs):
        if user['logged_in']:
            return func(*args,**kwargs)
        else:
            print("user is not logedin..")
    return wrapper


@login_required
def view_dashbord():
    print("Welcome Deshbord ")


user1={'logged_in':True}
user2={'logged_in':False}

view_dashbord(user1)
view_dashbord(user2)