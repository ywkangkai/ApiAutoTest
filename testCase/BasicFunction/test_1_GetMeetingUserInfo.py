import unittest
import json
import run_all_test
import jsonpath
from random import randint, choice
from requests_toolbelt import MultipartEncoder
from common.exceptHandler import ExceptResult
from common.httpRequrestHandler import GetApiResult
from common.assertHandler import AssertHandler
from common.xlsHandler import XlsHandlerConf
from data.interfaceInputData import RandomData
from data.interfaceInputData import fixed_meeting_room
from common.dataCleanHandler import DataCleanHandler
model_name = 'BasicFunction'
file_name = 'test_1_GetMeetingUserInfo.txt'
content_type = 'application/json;charset=UTF-8'
# 随机生成多个参会人员列表
name_list = [RandomData().random_user_name(), RandomData().random_user_name()]


def create_one_meeting():
    u'''创建一个会议并获取会议id'''
    tc_name = '创建一个会议并获取会议id'
    path = '/meeting/info'
    data = {"compereName": "",
            "doneDate": RandomData().get_date_after_today(),
            "meetingDate": "",
            "meetingRoomName": fixed_meeting_room,
            "name": RandomData().random_long_string(10),
            "needLogin": 0, "orderType": 0, "password": "",
            "userTypeList": [{"model": 1, "name": RandomData().random_long_string(5),
                              "userNames": name_list}],
            "teamStatus": choice([0, 2])
            }
    # print(data)
    api_result = GetApiResult().get_api_result_post(path, run_all_test.session, data, content_type)
    # print(api_result)
    ExceptResult().save_api_result_to_file(model_name, file_name, tc_name, api_result.text)
    response_text = json.loads(api_result.text, encoding='utf-8')  # 反馈结果的json字符串中的body部分
    return jsonpath.jsonpath(response_text, '$..meetingId')[0]


meeting_id = create_one_meeting()


def get_meeting_user_info():
    u'''获取参会人id信息'''
    tc_name = '获取参会人id信息'
    name_id_list = []
    for name in name_list:
        path = '/meeting/user/get/search'
        data = {"name": name}
        api_result = GetApiResult().get_api_result_get(path, run_all_test.session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, tc_name, api_result.text)
        response_text = json.loads(api_result.text, encoding='utf-8')  # 反馈结果的json字符串中的body部分
        name_id_list.append(jsonpath.jsonpath(response_text, '$..id')[0])
    return name_id_list


meeting_user_id = get_meeting_user_info()


class GetMeetingUserInfo(unittest.TestCase):
    u'''获取会议人员信息'''
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_1_meetingId_input_waitFor(self):
        u'''输入待进行的会议ID、不输入会议人员名称获取会议人员信息成功'''
        tc_name = '1-输入待进行的会议ID、不输入会议人员名称获取会议人员信息成功'
        path = '/meeting/ext/person'
        data = {"meetingId": meeting_id, 'name': ''}
        api_result = GetApiResult().get_api_result_get(path, run_all_test.session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, tc_name, api_result.text)
        response_text = json.loads(api_result.text, encoding='utf-8')  # 反馈结果的json字符串中的body部分
        self.assertEqual(api_result.status_code, 200)  # 断言我们的statues_code码是否为200
        AssertHandler().assert_body(response_text, 'result', 'message', 0, 'success')
        self.assertEqual(jsonpath.jsonpath(response_text, '$..personName')[0], name_list[0])  # 断言返回的数据中，参会人和添加的参会人员一致

    def test_2_meetingId_userName_input_exist(self):
        u'''输入待进行的会议ID、输入会议人员名称获取会议人员信息成功'''
        tc_name = '2-输入待进行的会议ID、输入会议人员名称获取会议人员信息成功'
        path = '/meeting/ext/person'
        data = {"meetingId": meeting_id, 'name': name_list[0]}
        api_result = GetApiResult().get_api_result_get(path, run_all_test.session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, tc_name, api_result.text)
        response_text = json.loads(api_result.text, encoding='utf-8')  # 反馈结果的json字符串中的body部分
        self.assertEqual(api_result.status_code, 200)  # 断言我们的statues_code码是否为200
        AssertHandler().assert_body(response_text, 'result', 'message', 0, 'success')
        self.assertEqual(jsonpath.jsonpath(response_text, '$..personName')[0], name_list[0])  # 断言返回的数据中，参会人和添加的参会人员一致

    def test_3_meetingId_input_onGoing(self):
        u'''输入进行中的会议ID、输入会议人员名称获取会议人员信息成功'''
        tc_name = '3-输入进行中的会议ID、输入会议人员名称获取会议人员信息成功'
        # 变更会议状态为进行中
        path = '/meeting/info/change/status' + '?meetingId=' + meeting_id + '&status=2'  # 改变会议状态为进行中
        data = {}
        api_result = GetApiResult().get_api_result_put(path, run_all_test.session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, '会议状态置为进行中', api_result.text)
        # 调用相应接口传参
        path = '/meeting/ext/person'
        data = {"meetingId": meeting_id, 'name': name_list[0]}
        api_result = GetApiResult().get_api_result_get(path, run_all_test.session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, tc_name, api_result.text)
        response_text = json.loads(api_result.text, encoding='utf-8')  # 反馈结果的json字符串中的body部分
        self.assertEqual(api_result.status_code, 200)  # 断言我们的statues_code码是否为200
        AssertHandler().assert_body(response_text, 'result', 'message', 0, 'success')
        # 断言返回的数据中，参会人和添加的参会人员一致
        self.assertEqual(jsonpath.jsonpath(response_text, '$..personName')[0], name_list[0])

    def test_4_meetingId_input_finished(self):
        u'''输入已结束的会议ID、不输入会议人员名称获取会议人员信息成功'''
        tc_name = '4-输入已结束的会议ID、不输入会议人员名称获取会议人员信息成功'
        # 变更会议状态为已结束
        path = '/meeting/info/change/status' + '?meetingId=' + meeting_id + '&status=3'  # 改变会议状态为已结束
        data = {}
        api_result = GetApiResult().get_api_result_put(path, run_all_test.session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, '会议状态置为已结束', api_result.text)
        # 调用相应接口传参
        path = '/meeting/ext/person'
        data = {"meetingId": meeting_id, 'name': ''}
        api_result = GetApiResult().get_api_result_get(path, run_all_test.session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, tc_name, api_result.text)
        response_text = json.loads(api_result.text, encoding='utf-8')  # 反馈结果的json字符串中的body部分
        self.assertEqual(api_result.status_code, 200)  # 断言我们的statues_code码是否为200
        AssertHandler().assert_body(response_text, 'result', 'message', 0, 'success')
        # 断言返回的数据中，参会人和添加的参会人员一致
        self.assertEqual(jsonpath.jsonpath(response_text, '$..personName')[0], name_list[0])

    def test_5_meetingId_input_notExist(self):
        u'''输入不存在的会议ID、不输入会议人员名称获取会议人员信息失败'''
        tc_name = '5-输入不存在的会议ID、不输入会议人员名称获取会议人员信息失败'
        path = '/meeting/ext/person'
        data = {"meetingId": RandomData().random_long_string(15), 'name': ''}
        api_result = GetApiResult().get_api_result_get(path, run_all_test.session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, tc_name, api_result.text)
        response_text = json.loads(api_result.text, encoding='utf-8')  # 反馈结果的json字符串中的body部分
        self.assertEqual(api_result.status_code, 200)  # 断言我们的statues_code码是否为200
        AssertHandler().assert_body(response_text, 'result', 'message', 0, 'success')
        # 断言我们获得的response中，data是否为空列表
        self.assertEqual(jsonpath.jsonpath(response_text, '$..data')[0], [])

    def test_6_meetingId_input_empty(self):
        u'''不输入会议ID获取会议人员信息失败'''
        tc_name = '6-不输入会议ID获取会议人员信息失败'
        path = '/meeting/ext/person'
        data = {"meetingId": '', 'name': ''}
        api_result = GetApiResult().get_api_result_get(path, run_all_test.session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, tc_name, api_result.text)
        response_text = json.loads(api_result.text, encoding='utf-8')  # 反馈结果的json字符串中的body部分
        self.assertEqual(api_result.status_code, 200)  # 断言我们的statues_code码是否为200
        AssertHandler().assert_body(response_text, 'result', 'message', -1, '会议Id不能为空')

    def test_7_admin_get_meetingUserInfo_success(self):
        '''超级管理员获取会议人员信息成功'''
        tc_name = '7-超级管理员获取会议人员信息成功'
        path = '/meeting/ext/person'
        data = {"meetingId": meeting_id, 'name': ''}
        api_result = GetApiResult().get_api_result_get(path, run_all_test.super_session, data, content_type)
        ExceptResult().save_api_result_to_file(model_name, file_name, tc_name, api_result.text)
        response_text = json.loads(api_result.text, encoding='utf-8')  # 反馈结果的json字符串中的body部分
        self.assertEqual(api_result.status_code, 200)  # 断言我们的statues_code码是否为200
        AssertHandler().assert_body(response_text, 'result', 'message', 0, 'success')
        # 断言返回的数据中，参会人和添加的参会人员一致
        self.assertEqual(jsonpath.jsonpath(response_text, '$..personName'), name_list)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        u'''删除刚新建的会议及会议人员'''
        # 删除会议
        DataCleanHandler().meeting_info_data_clean(meeting_id)
        # 删除人员
        for user_id in meeting_user_id:
            DataCleanHandler.meeting_user_data_clean(user_id)
