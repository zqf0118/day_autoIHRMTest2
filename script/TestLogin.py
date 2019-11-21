import unittest, logging
from api.loginApi import LoginApi
from utils import assert_utils


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        pass

    def tearDown(self) -> None:
        pass

    def test01_login_success(self):
        # 调用登陆接口
        response = self.login_api.login("13800000002", "123456")
        jsonData = response.json()  # type:dict
        logging.info("测试登陆成功返回的数据为： {}".format(jsonData))

        # # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, jsonData.get("success"))
        # self.assertEqual(10000, jsonData.get("code"))
        # self.assertIn("操作成功", jsonData.get("message"))
        # 调用断言函数
        assert_utils(self,
                     response, 200, True, 10000, "操作成功")

        token = jsonData.get("data")

    def test02_mobile_is_not_exist(self):
        # 调用登陆接口
        response = self.login_api.login("13900000002", "123456")
        # 打印数据
        jsonData = response.json()
        logging.info("测试用户名错误用例返回的数据为： {}".format(jsonData))
        # 断言
        assert_utils(self,
                     response,
                     200, False, 20001, "用户名或密码错误")

    def test03_password_is_error(self):
        # 调用登陆接口
        response = self.login_api.login("13800000002", "error")
        # 打印数据
        jsonData = response.json()
        logging.info("测试密码错误用例返回的数据为： {}".format(jsonData))
        # 断言
        assert_utils(self,
                     response,
                     200, False, 20001, "用户名或密码错误")

    def test04_mobile_is_empty(self):
        # 调用登陆接口
        response = self.login_api.login("", "error")
        # 打印数据
        jsonData = response.json()
        logging.info("测试用户名为空用例返回的数据为： {}".format(jsonData))
        # 断言
        assert_utils(self,
                     response,
                     200, False, 20001, "用户名或密码错误")

    def test05_password_is_empty(self):
        # 调用登陆接口
        response = self.login_api.login("13800000002", "")
        # 打印数据
        jsonData = response.json()
        logging.info("测试密码为空用例返回的数据为： {}".format(jsonData))
        # 断言
        assert_utils(self,
                     response,
                     200, False, 20001, "用户名或密码错误")

    def test06_requests_params_is_empty(self):
        # 调用无参的登陆接口
        response = self.login_api.login_params_is_null()
        # 打印数据
        jsonData = response.json()
        logging.info("测试无参的用例返回的数据为： {}".format(jsonData))
        # 断言
        assert_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")
