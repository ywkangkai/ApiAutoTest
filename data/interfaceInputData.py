from faker import Faker
import random
import os
from common import logHandler as myLogging
import datetime

fixed_meeting_room = '1303'


class RandomData:
    def __init__(self):
        global f, myLogger
        myLogger = myLogging.Logger()
        f = Faker(locale='zh_cn')

    # 随机产生想要长度的字符串
    def random_long_string(self, length):
        try:
            string = ''
            for i in range(length):
                random_string = f.random_letter()
                string = string + random_string
            return string
        except Exception as msg:
            myLogger.logger.error(msg)

    # 随机生成需要长度的数字
    def random_long_digit(self, length):
        try:
            number = ''
            for i in range(length):
                random_number = str(f.random_digit_not_null())
                number = number + random_number
            return int(number)
        except Exception as msg:
            myLogger.logger.error(msg)

    #  获取当天或以后的某一天的某个时间段
    def get_date_after_today(self):
        try:
            random_date = datetime.datetime.strftime(f.future_datetime(), '%Y-%m-%d %H:%M')  # 将日期格式化
            return random_date
        except Exception as msg:
            myLogger.logger.error(msg)

    #  随机获取某一天
    def get_date_random_day(self):
        try:
            random_date = datetime.datetime.strftime(f.date_time(), '%Y-%m-%d')  # 将日期格式化
            return random_date
        except Exception as msg:
            myLogger.logger.error(msg)

    #  获取随机某一年
    def get_random_year(self):
        try:
            random_year = datetime.datetime.strftime(f.future_datetime(), '%Y')  # 将日期格式化
            return random_year
        except Exception as msg:
            myLogger.logger.error(msg)

    # 随机文件扩展名
    def random_file_extension(self):
        try:
            extension = f.file_extension()
            return extension
        except Exception as msg:
            myLogger.logger.error(msg)

    # 生成随机姓名
    def random_user_name(self):
        try:
            user_name = f.name()
            return user_name
        except Exception as msg:
            myLogger.logger.error(msg)

    # 拼接一个随机的文件名
    def random_parse_file(self):
        try:
            file_name = f.file_name()
            result_file = file_name + RandomData().random_file_extension()
            return result_file
        except Exception as msg:
            myLogger.logger.error(msg)

    # 随机生成一串需要长度的特殊符号
    def random_a_sentence(self, length):
        result_sentence = '%^汉'
        try:
            for i in range(length-3):
                random_string = f.random_letter()
                result_sentence = result_sentence + random_string
            return result_sentence
        except Exception as msg:
            myLogger.logger.error(msg)

    # 随机生成一串需要长度的特殊符号
    def random_a_special_symbols(self, length):
        special_symbols = "~!@#$%^&*()_+:<>?/|\'\\.*+-[]={}"
        new_special_symbols = ""
        try:
            if length <= len(special_symbols):
                special_symbols = random.sample(special_symbols, length)
                for i in special_symbols:
                    new_special_symbols += i
                return new_special_symbols
            else:
                length = len(special_symbols)
                special_symbols = random.sample(special_symbols, length)
                for i in special_symbols:
                    new_special_symbols += i
                return new_special_symbols
        except Exception as msg:
            myLogger.logger.error(msg)

    # 以二进制读的方式返回需要上传的文件
    # file_name为需要指定在data目录下的某个文件名
    def get_upload_file_path(self, file_name):
        try:
            file_path = os.path.join(os.path.dirname(__file__), file_name)
            # files = {'file': open(file_path, 'rb')}
            return file_path
        except Exception as msg:
            myLogger.logger.error(msg)

    # 添加固定的会议室名称--后面的都会用
    def meeting_room_unified_name(self, length):
        try:
            str1 = RandomData().random_long_string(length)
            meeting_room_name = ''
            for i in str1:
                meeting_room_name += i
            return meeting_room_name
        except Exception as msg:
            myLogger.logger.error(msg)


if __name__ == "__main__":
    pass
    # a = RandomData().get_date_day()
    # print(a)