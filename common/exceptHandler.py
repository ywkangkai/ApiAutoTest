import os
import datetime
import common.logHandler as myLogging


class ExceptResult:
    def __init__(self):
        global myLogger
        myLogger = myLogging.Logger()

    # 将获取的api数据添加进入到apiResult中的某个文件中
    # 文件名和类型在用例中生成
    # modelName传入模块名称
    # fileName为result存储的文件名
    @staticmethod
    def save_api_result_to_file(model_name, file_name, test_name, result):
        filepath = os.path.join(os.path.join(os.path.join(os.path.dirname(
                   os.path.dirname(__file__)), 'apiResult'), model_name), file_name)
        result_list = [str(datetime.datetime.now()), ' ', test_name, '\n', result, '\n', '\n']
        try:
            with open(filepath, 'a+', encoding='utf-8') as fp:
                fp.writelines(result_list)
        except Exception as msg:
            myLogger.logger.error(msg)
