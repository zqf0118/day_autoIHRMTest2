import unittest, logging
from api.loginApi import LoginApi
from utils import assert_utils, read_login_data
from parameterized.parameterized import parameterized


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand(read_login_data)
    def test01_login(self, mobile, password, http_code, success, code, message):
        # 调用登陆接口
        response = self.login_api.login(mobile, password)
        jsonData = response.json()  # type:dict
        logging.info("测试登陆成功返回的数据为： {}".format(jsonData))

        # # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, jsonData.get("success"))
        # self.assertEqual(10000, jsonData.get("code"))
        # self.assertIn("操作成功", jsonData.get("message"))
        # 调用断言函数
        assert_utils(self,
                     response, http_code, success, code, message)
