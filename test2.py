import requests

def add(x, y):
    return x + y

def add2():
    print(add(1,1))
    print(add(1,2))
    print(add(1,3))

def login(obj, var1, var2, var3):
    return obj.post("http://localhost/index.php?m=Home&c=User&a=do_login",
                         data={"username": var1, "password": var2, "verify_code": var3})

def print_response(obj):
    print("print_response输出的内容： ",obj.json())


