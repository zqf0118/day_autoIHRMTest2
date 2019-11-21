import logging
import unittest
from api.loginApi import LoginApi
from api.empApi import EmpApi
from utils import assert_utils
import pymysql
from utils import DBUtils
import app


class TestEmp(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        cls.emp_api = EmpApi()
        print("初始化setUpClass")

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test01_login(self):
        # 调用登陆接口
        response = self.login_api.login("13800000002", "123456")
        # 获取token
        token = response.json().get("data")
        # headers
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        # 把获取到的Headers放在全局变量HEADERS中
        app.HEADERS = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        print(app.HEADERS)

    def test02_add_emp(self):
        # 调用添加员工接口
        response = self.emp_api.add_emp("乔布斯323432", "15388843234")
        logging.info("添加员工接口返回的值为： {}".format(response.json()))
        # 需要传入哪些参数？
        # 调用登陆接口，获取token，把token组合成Bearer xxx
        # requests.post(url, json=jsonData, headers=headers)

        # 断言：
        # self.assertEqual(200, respone.status_code)
        # self.assertEqual(True, respone.json().get("success"))
        # self.assertEqual(10000, respone.json().get("code"))
        # self.assertIn("操作成功", respone.json().get("message"))
        assert_utils(self, response, 200, True, 10000, "操作成功")

        # 保存员工ID到全局变量(app.py)
        jsonData = response.json()
        id = jsonData.get("data").get("id")
        # 实现保存员工ID到全局变量
        app.ID = id

    def test03_query_emp(self):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")

    def test04_update_emp(self):
        # 调用修改员工接口
        response = self.emp_api.update_emp("tom")
        logging.info("修改员工接口返回值为：{}".format(response.json()))
        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")

        # 断言数据库数据
        db = DBUtils(host="182.92.81.159", user='readuser', password="iHRM_user_2019", database="ihrm")
        with db as db:
            db.cursor.execute("select username from bs_user where id={} limit 1".format(app.ID))
            result = db.cursor.fetchall()
            logging.info("从数据库查询出来的员工名称是：{}".format(result[0][0]))
            # 断言数据库返回数据
            self.assertEqual("tom", result[0][0])

    def test05_delete_emp(self):
        # 调用修改员工接口
        response = self.emp_api.delete_emp()
        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")
