#--coding: utf-8-

import sys
import os
sys.path.append(os.getcwd()+'\cpy\cf')
import cf.函数
import cf.游览器
import datetime

# 获取当前日期
today = cf.函数.日期今天()

配置 = cf.函数.配置变量()

# 路径根据自己电脑配置
path = 配置['fangjia']['文件路径'] + '/' + str(datetime.datetime.now().year) + '房价/' + str(datetime.datetime.now().year) + '汇总/'

快照path = path+'快照/'
todayFile = path+today+'.json'

# 等待抓取快照
待抓取快照房源列表 = []

def makeDirs(info):
    小区path = 快照path+info['小区']+'/'
    cf.函数.新建文件夹(小区path)
    return ''

def 方法获取链接中的ID(url):
    start = url.rfind("/")
    end = url.rfind(".html")
    if start != -1 and end != -1:
        url = url[start+1 : end]
    return url

def 方法筛出待抓取快照房源(data):
    # 遍历小区列表
    for key in data['列表']:
        list = data['列表'][key]
        # 遍历小区房子
        for k in list:
            info = list[k]
            # 创建对应小区楼文件夹
            makeDirs(info)
            string = 方法获取链接中的ID(info['链接'])
            # 判断快照是否存在
            imageName = str(info['price'])+'--'+string+'.png'
            imageFile = 快照path+info['小区']+'/'+imageName
            if not os.path.exists(imageFile):
                待抓取快照房源列表.append(info)
    return ''

todayData = cf.函数.文件读取(todayFile)
if todayData != False:
    # 从json文件中读取数据
    方法筛出待抓取快照房源(todayData)
    if 待抓取快照房源列表 != []:
        driver = cf.游览器.游览器打开(['--window-size=1824,1026','--headless'])
        for info in 待抓取快照房源列表:
            print(info['链接'])
            driver.get(info['链接'])
            cf.函数.等待秒数(3)
            string = 方法获取链接中的ID(info['链接'])
            imageName = str(info['price'])+'--'+string+'.png'
            imageFile = 快照path+info['小区']+'/'+imageName
            print(imageFile)
            res = driver.save_screenshot(imageFile)
            print(res)
            print('完成快照')
            cf.函数.等待秒数(2)
        driver.quit()
        print('结束')
    else:
        print('没有')