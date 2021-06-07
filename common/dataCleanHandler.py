from common.httpRequrestHandler import GetApiResult
from common import logHandler as myLogging
import run_all_test

content_type = 'application/json;charset=UTF-8'


class DataCleanHandler:
    def __init__(self):
        global myLogger
        myLogger = myLogging.Logger()

    # 清理会议系统测试中遗留的部门信息
    @staticmethod
    def meeting_dept_data_clean(dept_id):
        try:
            path = "/meeting/dept/delete/" + str(dept_id)
            data = {}
            GetApiResult().get_api_result_delete(path, run_all_test.session, data, content_type)
        except Exception as msg:
            myLogger.logger.error(msg)

    # 清理会议系统测试中遗留的人员信息
    @staticmethod
    def meeting_user_data_clean(user_id):
        try:
            path = "/meeting/user/delete/" + str(user_id)
            data = {}
            GetApiResult().get_api_result_delete(path, run_all_test.session, data, content_type)
        except Exception as msg:
            myLogger.logger.error(msg)

    # 清理会议系统测试中遗留的会议室信息信息
    @staticmethod
    def meeting_room_data_clean(room_id):
        try:
            path = '/meeting/room/delete/' + str(room_id)
            data = {}
            GetApiResult().get_api_result_delete(path, run_all_test.session, data, content_type)
        except Exception as msg:
            myLogger.logger.error(msg)

    # 清理会议系统测试中遗留的机构信息信息
    @staticmethod
    def meeting_ent_data_clean(ent_id):
        try:
            path = '/system/ent' + '?entId=' + str(ent_id)
            data = {}
            GetApiResult().get_api_result_delete(path, run_all_test.super_session, data, content_type)
        except Exception as msg:
            myLogger.logger.error(msg)

    # 清理会议系统测试中遗留的会议
    @staticmethod
    def meeting_info_data_clean(meeting_id):
        try:
            path = '/meeting/info' + '?meetingId=' + str(meeting_id)
            data = {}
            GetApiResult().get_api_result_delete(path, run_all_test.session, data, content_type)
        except Exception as msg:
            myLogger.logger.error(msg)
    
    @staticmethod
    def managers_clean(managers_id):
        try:
            path = '/system/user' + '?id=' + str(managers_id)
            data = {}
            GetApiResult().get_api_result_delete(path, run_all_test.session, data, content_type)
        except Exception as msg:
            myLogger.logger.error(msg)
            
    # 清理会议系统测试中遗留的列席单位信息
    @staticmethod
    def unit_info_data_clean(unit_id):
        try:
            path = '/meeting/unit' + '?unitIds=' + str(unit_id)
            data = {}
            GetApiResult().get_api_result_delete(path, run_all_test.session, data, content_type)
        except Exception as msg:
            myLogger.logger.error(msg)


