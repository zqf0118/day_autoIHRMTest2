from unittest import TestCase
from requests import Response
import json, app, pymysql
import logging


# 封装数据库工具类
class DBUtils:
    def __init__(self, host=None, user=None, password=None, database=None, autocommit=None, charset='utf8'):
        # 初始化外部传入的数据库连接参数
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit
        self.charset = charset

    def __enter__(self):
        # 如果使用了with语法，就会执行以下语句，自动建立连接，获取游标
        # 如果获取连接失败，那么就不会有conn和cursor属性
        # 获取连接失败原因：域名不正确，用户名密码错误，服务器没有启动，数据库不正确等等
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.conn.cursor()
            return self
        except Exception as e:
            print("建立连接或者获取游标异常！： ", e)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 如果使用了with语法，就会自动执行以下语句，自动关闭游标和连接
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


# 通用断言
def assert_utils(self, response, htttpCode, success, code, message):
    """
    @type self:TestCase
    @type response:Response
    """
    # 断言httpcode
    print("assert_utils的selfid", id(self))
    jsonData = response.json()  # type:dict
    self.assertEqual(htttpCode, response.status_code)
    self.assertEqual(success, jsonData.get("success"))
    self.assertEqual(code, jsonData.get("code"))
    self.assertIn(message, jsonData.get("message"))


# 读取登陆数据
def read_login_data():
    app.init_logging()
    login_data = app.BASEDIR + "/data/login.json"
    with open(login_data, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        logging.info("read_login_data: {}".format(jsonData))
        result_list = []
        for data in jsonData:
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            result_list.append((mobile, password, http_code, success, code, message))
        logging.info("result_list: {}".format(result_list))
    return result_list


def read_add_emp():
    app.init_logging()
    add_emp_data_path = app.BASEDIR + "/data/emp_data.json"
    add_emp_result_list = []
    with open(add_emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        logging.info("读取的数据有：{}".format(jsonData))
        add_emp_data = jsonData.get("add_emp")
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        add_emp_result_list.append((username, mobile, http_code, success, code, message))
    logging.info("添加员工数据列表为：{}".format(add_emp_result_list))
    return add_emp_result_list

def read_query_emp():
    app.init_logging()
    query_emp_data_path = app.BASEDIR + "/data/emp_data.json"
    query_emp_result_list = []
    with open(query_emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        logging.info("读取的数据有：{}".format(jsonData))
        query_emp_data = jsonData.get("query_emp")
        http_code = query_emp_data.get("http_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        query_emp_result_list.append((http_code, success, code, message))
    logging.info("添加员工数据列表为：{}".format(query_emp_result_list))
    return query_emp_result_list


def read_update_emp():
    app.init_logging()
    update_emp_data_path = app.BASEDIR + "/data/emp_data.json"
    update_emp_result_list = []
    with open(update_emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        logging.info("读取的数据有：{}".format(jsonData))
        update_emp_data = jsonData.get("update_emp")
        update_username = update_emp_data.get("update_username")
        http_code = update_emp_data.get("http_code")
        success = update_emp_data.get("success")
        code = update_emp_data.get("code")
        message = update_emp_data.get("message")
        update_emp_result_list.append((update_username, http_code, success, code, message))
    logging.info("添加员工数据列表为：{}".format(update_emp_result_list))
    return update_emp_result_list


def read_delete_emp():
    app.init_logging()
    delete_emp_data_path = app.BASEDIR + "/data/emp_data.json"
    delete_emp_result_list = []
    with open(delete_emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        logging.info("读取的数据有：{}".format(jsonData))
        delete_emp_data = jsonData.get("delete_emp")
        http_code = delete_emp_data.get("http_code")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        delete_emp_result_list.append((http_code, success, code, message))
    logging.info("添加员工数据列表为：{}".format(delete_emp_result_list))
    return delete_emp_result_list

if __name__ == '__main__':
    read_delete_emp()
