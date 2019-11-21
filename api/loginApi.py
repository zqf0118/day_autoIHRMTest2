import requests


class LoginApi:

    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"

    def login(self, mobile, password):
        jsonData = {
            "mobile": mobile,
            "password": password
        }
        return requests.post(self.login_url, json=jsonData)

    def login_params_is_null(self):
        return requests.post(self.login_url)
