#--coding: utf-8-

import 函数

from selenium import webdriver

# 自动化专用chrome和chromedriver
# https://googlechromelabs.github.io/chrome-for-testing/#stable
# 下载chromedriver
# https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/win64/chromedriver-win64.zip
# 下载chrome
# https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/win64/chrome-win64.zip


conf = 函数.配置变量()


#------------------------------配置定义-------------------------------------------
# 设置 ChromeDriver 的路径，根据自己路径调整
chromedriver路径 = conf['游览器']['chromedriver路径']
# 设置 Chrome 的路径
chrome路径 = conf['游览器']['chrome路径']
#------------------------------配置定义end-------------------------------------------






#-------------------------------可用函数------------------------------------------

# 打开游览器 游览器options配置格式为数组 ['--headless','--window-size=1824,1026']
def 游览器打开(参数):
    游览器options = 游览器配置(参数)
    return webdriver.Chrome(options=游览器options, executable_path=chromedriver路径)

#-------------------------------可用函数end------------------------------------------








#-------------------------------以下为配置功能，一般情况下用不上-----------------------------------
# 游览器配置
def 游览器配置(参数=[]):
    # 游览器options.add_argument('--headless')  # 无头模式，即不打开浏览器窗口 # 快照抓取慢一般打开游览器
    # 游览器options.add_argument("--window-size=1824,1026") # 游览器大小
    游览器options = webdriver.ChromeOptions()
    游览器options.binary_location = chrome路径 # chrome路径
    for info in 参数:
        游览器options.add_argument(info)
    return 游览器options



