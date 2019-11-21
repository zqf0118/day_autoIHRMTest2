from test2 import add, add2,login, print_response
import requests

# 需求，实现输出1+1，1+2， 1+3

# print(1+1)
# print(1+2)
# print(1+3)
# print(add(1,1))
# print(add(1,2))
# print(add(1,3))

response = login(requests, "13800138006", "123456", "8888")
print_response(response)
