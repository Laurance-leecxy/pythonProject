# -*- coding:utf-8 -*-
# @文件名称  :funtion.py
# @项目名称  :Q4cal
# @软件名称  :PyCharm
# @创建时间  :2021-03-31 14:56
# @用户名称  :紫月孤忆
import datetime
import logging
import os


def getOneday(ti=1):
    """
    获取昨天日期
    :param ti:
    :return:
    """
    today = datetime.date.today()
    o_day = datetime.timedelta(days=ti)
    yesterday = today - o_day
    return yesterday


def jud_path(d_path, flag=True, is_establish=True) -> tuple:
    """
    判断路径是否存在，不存在直接创建
    :param is_establish: 判断是否创建路径
    :param flag:判断是否提示
    :param d_path:文件路径，自动去除不可加入文件名的（.）字符
    :return:返回路径属性，存在返回True，不存在返回False和创建的路径
    """
    __dps = d_path.split('/')
    if __dps[-1].index('.') + 1 != len(__dps[-1]):
        __dps = os.path.join(*__dps[:-1]).replace('\\', '/')
    else:
        __dps = d_path
    if os.path.isdir(__dps):
        return True, ''
    else:
        __route = None
        if flag:
            print('创建路径：', __dps)
        if is_establish:
            os.makedirs(__dps)
            __route = __dps
        return False, __route


def chect_dir(route):
    if not os.path.exists(route):
        os.makedirs(route)
    else:
        print('文件夹已存在:', route)


def write_log(message, route, mod='deb'):
    """
    品牌新享日志
    :return:
    """
    dt = getOneday(1)
    month = dt.month
    year = dt.year
    filename = os.path.join(route, str(year)).replace('\\', '/')
    chect_dir(filename)
    if mod == 'deb':
        filename += '/deblog'
    elif mod == 'inf':
        filename += '/inflog'
    elif mod == 'war':
        filename += '/warlog'
    else:
        filename += '/crilog'

    filename += str(year) + '-' + str(month) + '.log'
    fmt = '%(asctime)s :(%(levelname)s) [line:%(lineno)d] %(message)s'
    level = "DEBUG"
    logger = None
    handler_file = None
    try:
        formatter = logging.Formatter(fmt)
        logger = logging.getLogger('myloger')
        logger.setLevel(logging.DEBUG)

        handler_file = logging.FileHandler(filename)
        handler_file.setFormatter(formatter)
        handler_file.setLevel(level)

        handler_console = logging.StreamHandler()
        handler_console.setFormatter(formatter)
        handler_console.setLevel(level)

        # 给logger添加handler
        logger.addHandler(handler_file)
        if mod == 'deb':
            logger.debug(message)
        elif mod == 'inf':
            logger.info(message)
        elif mod == 'war':
            logger.warning(message)
        else:
            logger.critical(message)
    except BaseException as e:
        print(e)
        print('日志写入错误，请及时检查，对已插入的')
    finally:
        logger.removeHandler(handler_file)  # 清除日志句柄里面的日志信息
