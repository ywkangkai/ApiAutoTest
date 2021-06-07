import os
import configparser
import common.logHandler as myLogging


class ConfigSetting:
    def __init__(self):
        global myLogger, cf
        cf = configparser.ConfigParser()
        confdir = os.path.join(os.path.dirname(__file__), 'config.ini')
        myLogger = myLogging.Logger()
        try:
            cf.read(confdir,encoding='utf-8')
        except Exception as msg:
            myLogger.logger.error(msg)

    # 通过代码写入config,ini中的一组配置
    def writeIni(self, filePath, section, **kwargs):
        try:
            cf.add_section(section)
            for key in kwargs:
                cf.set(section, key, kwargs[key])
            cf.write(open(filePath), 'w')
        except Exception as msg:
            myLogger.logger.error(msg)

    # 通过代码更新config,ini中的一组配置
    def updateIni(self, filePath, section, **kwargs):
        try:
            for key in kwargs:
                cf.set(section, key, kwargs[key])
            cf.write(open(filePath), 'w')
        except Exception as msg:
            myLogger.logger.error(msg)

    # 获取config,ini中的一组配置
    def getOneOptions(self, section, option):
        try:
            optioninfo = cf.get(section, option)
            return optioninfo
        except Exception as msg:
            myLogger.logger.error(msg)
