# 1 导包
import app
import unittest
import time
from script.TestEmpParams import TestEmp
from script.TestLoginParams import TestLogin

# 2 初始化测试套件
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
# 3 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))
# 4 生成测试报告
# 定义测试报告的名称
print("BaseDir的值：", app.BASEDIR)
report_name = app.BASEDIR + "/report/ihrm-{}.html".format(time.strftime('%Y%m%d %H%M%S'))
with open(report_name, mode='wb') as f:
    # 定义htmltestrunner的实例
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源管理系统测试报告", description="登陆模块的测试")
    #　使用runner运行测试套件
    runner.run(suite)
