# 1 导包
import logging
from logging import handlers
import os
import requests

BASEDIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {}
ID = 0

def init_logging():
    # 2 创建日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.INFO)
    # 4 创建处理器
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    log_name = BASEDIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_name, when='D', interval=1, backupCount=7, encoding='utf-8')

    # 5 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 6 将格式化器添加到处理器
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    # 7 将处理器添加到日志器
    logger.addHandler(fh)
    logger.addHandler(sh)


# 获取token
def get_token():
    # 调用登陆接口
    response = requests.post("http://182.92.81.159/api/sys/login", json={"mobile": "13800000002", "password": "123456"})
    # 获取响应数据
    jsonData = response.json()
    logging.info(jsonData)
    # 获取token
    token = jsonData.get("data")
    return token


if __name__ == '__main__':
    init_logging()
