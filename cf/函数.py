#--coding: utf-8-

# 使用条件需加载路径
# import sys
# import os
# sys.path.append(os.getcwd()+'\cpy\cf')
# import cf
# 调用方式 cf.函数.日期今天()

import requests
import json
import time
import os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# 获取配置项
def 配置变量():
    return 文件读取('./cpy/cf/conf.json')


def 等待秒数(seconds=1):
    time.sleep(seconds)
    return ''

def 日期今天():
    return str(datetime.now().date())

def 日期昨天():
    today = datetime.now().date()
    return str((today - timedelta(days=1)))

# 递归新建文件夹
def 新建文件夹(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return ''

# 过滤换行和多余空格
def 字符串格式化(string=''):
    return string.strip().replace('\n', '').replace(' ', '').replace('\r', '')

# 读取文件 文件路径，文件类型
def 文件读取(file, type='json'):
    文件内容 = False
    if os.path.exists(file):
        with open(file, "r", encoding='utf-8') as f:
            文件内容 = f
            if type == 'json':
                文件内容 =  json.load(f)
    return 文件内容

# 写入文件 文件路径，文件内容
def 文件写入(file, data):
    path = os.path.dirname(file)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(file, "w", encoding='utf-8') as f:
        f.write(data)
    return ''

# 方便查看json数据
def json格式化展示(data):
    return json.dumps(data, indent=4, ensure_ascii=False)

# 获取html代码
def html获取soup(url):
    response = requests.get(url)
    # 获取响应内容
    content = response.text
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser')
    return soup

# 判断文件是否存在
def 文件是否存在(file):
    return os.path.exists(file)

# 字符串是否含有
def 字符串是否含有(string1 = '', string2 = ''):
    result = False
    if string2 in string1:
        result =  True
    return result
