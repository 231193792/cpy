#--coding: utf-8-



# 图像操作
# 安装图片识别、点击组件
# pip install opencv-python
# pip install pyautogui

# # test.py文件
# import cv2
# import pyautogui
# # 加载指定图像
# image = cv2.imread('test.png')
# # 在屏幕上找到图像的位置
# position = pyautogui.locateOnScreen(image)
# # 单击
# pyautogui.click(position)
# # 双击
# pyautogui.doubleClick(position)


# 使用条件需加载路径
import cf.函数
import cv2
import pyautogui


# 点击图像
def 点击图像(待识别图片文件路径, 点击类型=1, 识别后延迟点击秒数=0):
    位置信息 = 识别图像(待识别图片文件路径)
    if 位置信息:
        cf.函数.等待秒数(识别后延迟点击秒数)
        if 点击类型 == 2:
            pyautogui.doubleClick(位置信息)
        else:
            pyautogui.click(位置信息)
        print('执行点击')
        return True
    else:
        return False


#-------------------------------以下为配置功能，一般情况下用不上-----------------------------------
# 识别图像
def 识别图像(待识别图片文件路径):
    # 判断文件是否存在
    if cf.函数.文件是否存在(待识别图片文件路径):
        image = cv2.imread(待识别图片文件路径)
        位置信息 = pyautogui.locateOnScreen(image)
        if 位置信息:
            print("找到图像"+待识别图片文件路径)
            return 位置信息
        else:
            print("false")
            return 位置信息
    else:
        print('文件不存在')
        return False