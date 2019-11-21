import requests
import app


class EmpApi:

    def __init__(self):
        self.add_emp_url = "http://182.92.81.159/api/sys/user"
        self.query_emp_url = "http://182.92.81.159/api/sys/user"
        self.update_emp_url = "http://182.92.81.159/api/sys/user"
        print("员工管理模块API__init__方法调用")

    def add_emp(self, username, mobile):
        headers = app.HEADERS
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-11-01",
            "formOfEmployment": 1,
            "workNumber": "33333222",
            "departmentName": "测试部",
            "correctionTime": "2019-11-18T16:00:00.000Z"
        }
        print("app.HEADERS", app.HEADERS)
        return requests.post(self.add_emp_url, json=jsonData, headers=headers)

    def query_emp(self):
        headers = app.HEADERS
        id = app.ID
        url = self.query_emp_url + "/" + id
        print("查询员工的URL为：{}".format(url))
        return requests.get(url, headers=headers)

    def update_emp(self, username):
        headers = app.HEADERS
        id = app.ID
        url = self.update_emp_url + "/" + id
        print("update_emp: ", url)
        print("headers: ", headers)
        return requests.put(url, json={"username": username}, headers=headers)

    def delete_emp(self):
        headers = app.HEADERS
        id = app.ID
        url = self.update_emp_url + "/" + id
        return requests.delete(url, headers=headers)
