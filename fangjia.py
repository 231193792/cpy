#--coding: utf-8-
import sys
import os
sys.path.append(os.getcwd()+'\cpy\cf')
import cf.函数
import datetime

配置 = cf.函数.配置变量()

# 路径根据自己电脑配置
path = 配置['fangjia']['文件路径'] + '/' + str(datetime.datetime.now().year) + '房价/'

# 搜索栏小区关键词 {"小区":"小区名(用于命名文件夹作为小区唯一标识)","链接":"对应小区根据条件查询完的链接，直接复制即可"}
# 此处为3房 总价从低到高，在查询完直接复制url
小区列表 = 配置['fangjia']['小区列表']

# 获取当前日期
today = str(cf.函数.日期今天())

# 计算昨天的日期
yesterday = str(cf.函数.日期昨天())

def 方法今日与昨天对比(data, yesterday):
    if yesterday == False:
        return data
    count = 1
    # 判断今天与昨天对比
    for key in data['列表']:
        info = data['列表'][key]
        if count == 1:
            # 获取小区第一个判断为最低价
            数据汇总['最低价'] = 数据汇总['最低价']+[key+info['小区']+'最低价'+info['price']]
            count += 1
        if key in yesterday['列表']:
            if info['price'] > yesterday['列表'][key]['price']:
                # 涨价
                data['信息']['涨价'] = data['信息']['涨价'] + [key+info['小区']+'涨价了，'+yesterday['列表'][key]['price']+'->'+info['price']]
            elif info['price'] < yesterday['列表'][key]['price']:
                # 降价
                data['信息']['降价'] = data['信息']['降价'] + [key+info['小区']+'降降降降降降价了！！！，'+yesterday['列表'][key]['price']+' --> '+info['price']]
        else:
            # 新增
            data['信息']['新增'] = data['信息']['新增'] + [key+info['小区']+'新增房源，'+info['price']]
    # 判断昨天与今天对比
    for key in yesterday['列表']:
        info = yesterday['列表'][key]
        if key not in data['列表']:
            #下架
            data['信息']['下架'] = data['信息']['下架'] + [key+info['小区']+'下架了，下架前价格'+yesterday['列表'][key]['price']]
    return data

# 数据汇总
数据汇总 = {
    '日期':today,
    '最低价':[],
    '信息':{'降价':[],'新增':[],'涨价':[],'下架':[]},
    '列表':{},
}


for 小区详情 in 小区列表:
    # 获取小区及创建文件夹
    小区 = 小区详情['小区']
    cf.函数.新建文件夹(path+小区)
    url = 小区详情['链接']
    print(小区)
    # 请求获取url对应html代码
    soup = cf.函数.html获取soup(url)
    cf.函数.等待秒数(2)
    # 找到房源列表tag
    p_tags = soup.find('ul', class_='sellListContent')
    p_tags = p_tags.find_all('div', class_='info clear')
    # 定义小区变量
    数据小区今天 = {
        '小区':小区,
        '日期':today,
        '信息':{'降价':[],'新增':[],'涨价':[],'下架':[]},
        '列表':{}
    }
    count = 1
    # 遍历网页房源列表
    # 获取排序20的价位对比后面的价位，相同保留，不相同全过滤，防止同价位排混乱
    保留价钱 = 999999
    for a in p_tags:
        当前房源价钱 = cf.函数.字符串格式化(a.find('div', class_='totalPrice').text).replace('万', '')
        if count == 20:
            保留价钱 = 当前房源价钱
        if count > 20 and 当前房源价钱 != 保留价钱:
            break
        count += 1
        # 获取html代码标签中的text
        positionInfo = a.find('div', class_='positionInfo').find('a').text
        href     = a.find('a', class_='maidian-detail').get('href').strip().replace('\n', '').replace(' ', '')
        title    = a.find('div', class_='title').text
        price    = a.find('div', class_='totalPrice').text
        avgPrice = a.find('div', class_='unitPrice').text
        putTime  = a.find('div', class_= 'followInfo').text
        houseInfo = a.find('div', class_='houseInfo').text
        # 格式化过滤换行符及多余空格
        数据小区今天['列表'][href] = {
            '序号': (count-1),
            'price':cf.函数.字符串格式化(price).replace('万', ''),
            '价格'  : cf.函数.字符串格式化(price),
            '均价'  : cf.函数.字符串格式化(avgPrice),
            '房子信息': cf.函数.字符串格式化(houseInfo),
            '发布时间': cf.函数.字符串格式化(putTime),
            '标题'  : cf.函数.字符串格式化(title),
            '小区'  : cf.函数.字符串格式化(positionInfo),
            '链接'  : cf.函数.字符串格式化(href),
        }
    # 今天与昨天文件数据路径
    昨天数据file = path+小区+'/'+小区+yesterday+'.json'
    今天数据file = path+小区+'/'+小区+today+'.json'
    # 读取昨天数据
    数据小区昨天 = cf.函数.文件读取(昨天数据file)
    # 对比今天昨天数据
    数据小区今天 = 方法今日与昨天对比(数据小区今天, 数据小区昨天)
    # 把今天小区数据合并一份到汇总数据
    数据汇总['信息']['降价'] = 数据汇总['信息']['降价']+数据小区今天['信息']['降价']
    数据汇总['信息']['新增'] = 数据汇总['信息']['新增']+数据小区今天['信息']['新增']
    数据汇总['信息']['涨价'] = 数据汇总['信息']['涨价']+数据小区今天['信息']['涨价']
    数据汇总['信息']['下架'] = 数据汇总['信息']['下架']+数据小区今天['信息']['下架']
    数据汇总['列表'][小区] = 数据小区今天['列表']
    # 写入今天数据
    cf.函数.文件写入(今天数据file, cf.函数.json格式化展示(数据小区今天))

# 汇总数据写入
数据汇总File = path+'2023汇总/'+today+'.json'
cf.函数.文件写入(数据汇总File, cf.函数.json格式化展示(数据汇总))

print('结束')