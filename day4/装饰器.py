def login(func):
    def inner(arg):
        print("passed user verification...")
        func(arg)
    return inner

def home():
    print("Welcome [%s] to home page" )
@login
def tv(name):
    print("Welcome [%s] to TV page" %name)

# tv = login(tv)
tv("Alex")