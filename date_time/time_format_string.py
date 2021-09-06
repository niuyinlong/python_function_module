import re
from datetime import datetime


class DateStandardization:

    def __init__(self, date_time):
        self.date_time = date_time  # date_time为日期格式字符串

    def year_month_day_hour_minute_second(self, x):
        """
        该方法可以识别日期格式字符串：年月日 时分秒，转化为标准日期格式字符串：年-月-日 时:分:秒，返回标准化后的日期格式字符串
        """
        year_month_day_hour_minute_second = r'20\d{2}[/-]{1}(([01]\d{1})|(\d{1}))[/-]{1}(([0123]{1}\d{1})|(\d{1}))\s{1,2}(([012]\d{1})|(\d{1}))[:]{1}(([012345]{1}\d{1})|(\d{1}))[:]{1}(([012345]{1}\d{1})|(\d{1}))'
        x = re.search(year_month_day_hour_minute_second, x).group()  # 获取标准时间年月日 时分秒
        x = datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
        x = x.strftime('%Y-%m-%d %H:%M:%S')
        return x

    def year_month_day_hour_minute(self, x):
        """
        该方法可以识别日期格式字符串：年月日 时分，转化为标准日期格式字符串：年-月-日 时:分:秒，返回标准化后的日期格式字符串
        """
        year_month_day_hour_minute = r'20\d{2}[/-]{1}(([01]\d{1})|(\d{1}))[/-]{1}(([0123]{1}\d{1})|(\d{1}))\s{1,2}(([012]\d{1})|(\d{1}))[:]{1}(([012345]{1}\d{1})|(\d{1}))'
        x = re.search(year_month_day_hour_minute, x).group()  # 获取标准时间年月日 时分
        x = datetime.strptime(x, '%Y-%m-%d %H:%M')
        x = x.strftime('%Y-%m-%d %H:%M:%S')
        return x

    def month_day_year_hour_minute_second(self, x):
        """
        该方法可以识别日期格式字符串：月日年 时分秒，转化为标准日期格式字符串：年-月-日 时:分:秒，返回标准化后的日期格式字符串
        """
        month_day_year_hour_minute_second = r'(([01]\d{1})|(\d{1}))[/-]{1}(([0123]{1}\d{1})|(\d{1}))[/-]{1}20\d{2}\s{1,2}(([012]\d{1})|(\d{1}))[:]{1}(([012345]{1}\d{1})|(\d{1}))[:]{1}(([012345]{1}\d{1})|(\d{1}))'
        x = re.search(month_day_year_hour_minute_second, x).group()  # 获取时间月日年 时分秒
        x = datetime.strptime(x, '%m-%d-%Y %H:%M:%S')
        x = x.strftime('%Y-%m-%d %H:%M:%S')
        return x

    def month_day_year_hour_minute(self, x):
        """
        该方法可以识别日期格式字符串：月日年 时分，转化为标准日期格式字符串：年-月-日 时:分:秒，返回标准化后的日期格式字符串
        """
        month_day_year_hour_minute = r'(([01]\d{1})|(\d{1}))[/-]{1}(([0123]{1}\d{1})|(\d{1}))[/-]{1}20\d{2}\s{1,2}(([012]\d{1})|(\d{1}))[:]{1}(([012345]{1}\d{1})|(\d{1}))'
        x = re.search(month_day_year_hour_minute, x).group()  # 获取时间月日年 时分
        x = datetime.strptime(x, '%m-%d-%Y %H:%M')
        x = x.strftime('%Y-%m-%d %H:%M:%S')
        return x

    def day_month_year_hour_minute_second(self, x):
        """
        该方法可以识别日期格式字符串：日月年 时分秒，转化为标准日期格式字符串：年-月-日 时:分:秒，返回标准化后的日期格式字符串
        """
        day_month_year_hour_minute_second = r'(([0123]{1}\d{1})|(\d{1}))[/-]{1}(([01]\d{1})|(\d{1}))[/-]{1}20\d{2}\s{1,2}(([012]\d{1})|(\d{1}))[:]{1}(([012345]{1}\d{1})|(\d{1}))[:]{1}(([012345]{1}\d{1})|(\d{1}))'
        x = re.search(day_month_year_hour_minute_second, x).group()  # 获取时间日月年 时分秒
        x = datetime.strptime(x, '%d-%m-%Y %H:%M:%S')
        x = x.strftime('%Y-%m-%d %H:%M:%S')
        return x

    def day_month_year_hour_minute(self, x):
        """
        该方法可以识别日期格式字符串：日月年 时分，转化为标准日期格式字符串：年-月-日 时:分:秒，返回标准化后的日期格式字符串
        """
        day_month_year_hour_minute = r'(([0123]{1}\d{1})|(\d{1}))[/-]{1}(([01]\d{1})|(\d{1}))[/-]{1}20\d{2}\s{1,2}(([012]\d{1})|(\d{1}))[:]{1}(([012345]{1}\d{1})|(\d{1}))'
        x = re.search(day_month_year_hour_minute, x).group()  # 获取时间日月年 时分
        x = datetime.strptime(x, '%d-%m-%Y %H:%M')
        x = x.strftime('%Y-%m-%d %H:%M:%S')
        return x


class DateTimeFunctions(DateStandardization):

    def ymd(self):
        """
        该方法可以识年月日 时分秒，年月日 时分，2种日期格式字符串，不符合上述2种情况，认定为非日期格式字符串
        """
        try:
            date_time = self.date_time.replace(re.search(r'[/-]{1}', self.date_time).group(), '-')  # 标准化日期格式中的分隔符为-
            # 根据分隔符-切割出来的第一个位置的数字长度等于4，则认为该时间格式为年开头
            if len(date_time.split('-', 1)[0]) == 4:
                try:
                    x = self.year_month_day_hour_minute_second(date_time)  # 处理年月日 时分秒日期格式的字符串
                    return x
                except AttributeError as e:
                    print('报错信息：{}'.format(e))
                    x = self.year_month_day_hour_minute(date_time)  # 处理年月日 时分 日期格式的字符串
                    return x
        except Exception as e:
            print('{}不是日期格式字符串，报错信息:{}'.format(self.date_time, e))

    def mdy(self):
        """
        该方法可以识月日年 时分秒，月日年 时分，2种日期格式字符串，不符合上述2种情况，认定为非日期格式字符串
        """
        try:
            date_time = self.date_time.replace(re.search(r'[/-]{1}', self.date_time).group(), '-')  # 标准化日期格式中的分隔符为-
            # 根据分隔符-切割出来的第一个位置的数字长度小于等于2，则认为该时间格式为月开头或日开头
            if len(date_time.split('-', 1)[0]) <= 2:
                try:
                    x = self.month_day_year_hour_minute_second(date_time)  # 处理月年日 时分秒日期格式的字符串
                    return x
                except AttributeError as e:
                    print('报错信息：{}'.format(e))
                    x = self.month_day_year_hour_minute(date_time)  # 处理月年日 时分日期格式的字符串
                    return x
        except Exception as e:
            print('{}不是日期格式字符串，报错信息:{}'.format(self.date_time, e))

    def dmy(self):
        """
        该方法可以识日月年 时分秒，日月年 时分，2种日期格式字符串，不符合上述2种情况，认定为非日期格式字符串
        """
        try:
            date_time = self.date_time.replace(re.search(r'[/-]{1}', self.date_time).group(), '-')  # 标准化日期格式中的分隔符为-
            # 根据分隔符-切割出来的第一个位置的数字长度小于等于2，则认为该时间格式为月开头或日开头
            if len(date_time.split('-', 1)[0]) <= 2:
                try:
                    x = self.day_month_year_hour_minute_second(date_time)  # 处理日月年 时分秒日期格式的字符串
                    return x
                except AttributeError as e:
                    print('报错信息：{}'.format(e))
                    x = self.day_month_year_hour_minute(date_time)  # 处理日月年 时分日期格式的字符串
                    return x
        except Exception as e:
            print('{}不是日期格式字符串，报错信息:{}'.format(self.date_time, e))

    def ymd_and_mdy(self):
        """
        该方法可以识年月日 时分秒，年月日 时分，月日年 时分秒，月日年 时分，4种日期格式字符串，不符合上述4种情况，认定为非日期格式字符串
        """
        try:
            date_time = self.date_time.replace(re.search(r'[/-]{1}', self.date_time).group(), '-')  # 标准化日期格式中的分隔符为-
            # 根据分隔符-切割出来的第一个位置的数字长度等于4，则认为该时间格式为年开头
            if len(date_time.split('-', 1)[0]) == 4:
                try:
                    x = self.year_month_day_hour_minute_second(date_time)  # 处理年月日 时分秒日期格式的字符串
                    return x
                except AttributeError as e:
                    print('报错信息：{}'.format(e))
                    x = self.year_month_day_hour_minute(date_time)  # 处理年月日 时分 日期格式的字符串
                    return x
            # 根据分隔符-切割出来的第一个位置的数字长度小于等于2，则认为该时间格式为月开头或日开头，目前无法根据代码判断具体是哪种类型
            elif len(date_time.split('-', 1)[0]) <= 2:
                try:
                    x = self.month_day_year_hour_minute_second(date_time)  # 处理月日年 时分秒日期格式的字符串
                    return x
                except AttributeError as e:
                    print('报错信息：{}'.format(e))
                    x = self.month_day_year_hour_minute(date_time)  # 处理月日年 时分日期格式的字符串
                    return x
        except Exception as e:
            print('{}不是日期格式字符串，报错信息:{}'.format(self.date_time, e))

    def ymd_and_dmy(self):
        """
        该方法可以识年月日 时分秒，年月日 时分，日月年 时分秒，日月年 时分，4种日期格式字符串，不符合上述4种情况，认定为非日期格式字符串
        """
        try:
            date_time = self.date_time.replace(re.search(r'[/-]{1}', self.date_time).group(), '-')  # 标准化日期格式中的分隔符为-
            # 根据分隔符-切割出来的第一个位置的数字长度等于4，则认为该时间格式为年开头
            if len(date_time.split('-', 1)[0]) == 4:
                try:
                    x = self.year_month_day_hour_minute_second(date_time)  # 处理年月日 时分秒日期格式的字符串
                    return x
                except AttributeError as e:
                    print('报错信息：{}'.format(e))
                    x = self.year_month_day_hour_minute(date_time)  # 处理年月日 时分 日期格式的字符串
                    return x
            # 根据分隔符-切割出来的第一个位置的数字长度小于等于2，则认为该时间格式为月开头或日开头，目前无法根据代码判断具体是哪种类型
            elif len(date_time.split('-', 1)[0]) <= 2:
                try:
                    x = self.day_month_year_hour_minute_second(date_time)  # 处理日月年 时分秒日期格式的字符串
                    return x
                except AttributeError as e:
                    print('报错信息：{}'.format(e))
                    x = self.day_month_year_hour_minute(date_time)  # 处理日月年 时分日期格式的字符串
                    return x
        except Exception as e:
            print('{}不是日期格式字符串，报错信息:{}'.format(self.date_time, e))


if __name__ == '__main__':
    date_str = '2011/1/1 2:3:4'
    ym_date = DateTimeFunctions(date_str)
    print(ym_date.ymd())
