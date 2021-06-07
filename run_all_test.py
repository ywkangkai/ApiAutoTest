# -*- coding: utf-8 -*-
import os
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import common.logHandler as myLogging
from common.getCookieHandler import GetCookieResult
import configHandler

# test_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testCase'), 'model1')
session = GetCookieResult().get_login_cookie()
super_session = GetCookieResult().get_super_admin_cookie()
manager1_session = GetCookieResult().managerSession(1)
manager2_session = GetCookieResult().managerSession(2)
manager3_session = GetCookieResult().managerSession(3)

'''
file = open(r'public_session.txt', mode='w')
file.write(session)
file.close()
'''
report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'report')
myLogger = myLogging.Logger()


# 传入model_name只执行该model中的部分用例
# 如果model_name值为空列表则执行testCase中的所有用例
def define_case_path(model_name):
    # 所有模块的名称
    '''
    'ProcessManage'：流程
    'UserInfoLibrary'：数据管理-与会人员信息库
    'DeptInfoTest'：数据管理-部门信息
    'MeetingRoomInfoTest':数据管理-会议室信息
    'DataExport'：数据管理-数据导出
    'DataImport'：数据管理-数据导入
    'InstitutionManagementTest':系统管理-会议管理机构管理
    'InstitutionParameter'：机构管理中心-机构参数
    'DataBackupTest'：系统管理-数据备份
    'SystemParamsSet'：系统管理-系统参数设置
    'DiskSpace'：系统管理-磁盘空间
    'SoftwareServices':系统管理-软件服务
    'LoginAndLogoutTest'：用户认证-登入登出
    'FunctionPlugInQueryTest'：通用接口-功能插件查询
    'OptionVote'：会中交互-意见表决
    'MeetingNamed':会中交互-点名
    'SentMessage':会中交互-消息发送
    'BasicFunction':会中交互-基础功能接口
    'MeetingSginIn':签到下载
    'MeetingInfo'：会议管理-会议信息
    'UploadMeetingFile':会议管理-会议文件
    'MeetingTopics'：会议管理-议题信息
    'DataStatistic'：主页-数据统计
    'CreateCoordinationOrganizationalStructure':协同建会组织架构
    'UnitInfo'：列席单位
    '''
    all_model_name = ['UnitInfo', 'MeetingInfo',
                      'OptionVote', 'MeetingNamed', 'SentMessage', 'DeptInfoTest',
                      'MeetingTopics', 'UserInfoLibrary', 'SystemParamsSet', 'DataExport',
                      'DataImport', 'BasicFunction', 'UploadMeetingFile', 'InstitutionParameter',
                      'InstitutionManagementTest', 'HomeDataStatistics',
                      'ProcessManage', 'DiskSpace',
                      'MeetingRoomInfoTest', 'FunctionPlugInQueryTest', 'FilePostStation', 'FilePostStationServer']
    '''

    all_model_name = ['CreateCoordinationOrganizationalStructure', 'CreateCoordinationMeeting', 'DataExport',
                      'DataImport', 'UserInfoLibrary', 'SystemParamsSet', 'InstitutionParameter',
                      'InstitutionManagementTest', 'DeptInfoTest', 'MeetingRoomInfoTest', 'FunctionPlugInQueryTest']
    '''
    '''
    all_model_name = ['MeetingRoomInfoTest']
    '''
    try:
        if model_name != []:
            test_path_all = []
            for i in range(len(model_name)):
                if model_name[i] in all_model_name:
                    test_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testCase'), model_name[i])
                    test_path_all.append(test_path)
                else:
                    print(model_name[i] + "   模块不存在")
            return test_path_all
        else:
            test_path_all = []
            for i in range(len(all_model_name)):
                test_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testCase'), all_model_name[i])
                test_path_all.append(test_path)
            return test_path_all

    except Exception as msg:
        myLogger.logger.error(msg)


# 执行所有模块或部分模块中的测试用例
def run_model_test_case(model_name):
    try:
        test_path_all = define_case_path(model_name)
        test_unit = unittest.TestSuite()
        for i in range(len(test_path_all)):
            discover = unittest.TestLoader().discover(test_path_all[i], pattern='test_*.py', top_level_dir=None)
            for suite in discover:  # 使用for循环出suite,再循环出case
                for case in suite:
                    try:
                        test_unit.addTests(case)
                    except Exception as msg:
                        print(msg, case, end="")
                        print("接口用例出现异常！")
        return test_unit
    except Exception as msg:
        myLogger.logger.error(msg)


# 执行testCase目录中.py文件名称为test_开头文件中的用例
def run_all_test_case():
    try:
        test_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testCase')
        discover = unittest.defaultTestLoader.discover(test_path, pattern='test_*.py', top_level_dir=None)
        return discover
    except Exception as msg:
        myLogger.logger.error(msg)


# 获取最终报告文件地址
def get_last_report_file(report_dir):
    try:
        file_list = os.listdir(report_dir)
        file_list.sort(key=lambda fn: os.path.getmtime(report_dir + '\\' + fn))
        last_file_path = os.path.join(report_dir, file_list[-1])
        return last_file_path
    except Exception as msg:
        myLogger.logger.error(msg)


# 携带文件并发送邮件到指定的邮箱中
def send_email(file_path):
    try:
        with open(file_path, 'rb') as fp:
            email_body = fp.read()
        message = MIMEMultipart()
        message_html = MIMEText(email_body, 'html', 'utf-8')
        message_html['Content-Type'] = 'application/octet-stream'
        message_html['Content-Disposition'] = 'attactment;filename="autoTestReport.html"'
        txt = MIMEText(u'2.6.0自动化测试报告', 'plain', 'utf-8')
        message.attach(message_html)
        message.attach(txt)

        cf = configHandler.ConfigSetting()

        smtp = smtplib.SMTP('smtp.163.com')
        message['From'] = cf.getOneOptions('Email', 'sender')
        message['To'] = ';'.join(cf.getOneOptions('Email', 'receiver').split(','))
        message['subject'] = Header(cf.getOneOptions('Email', 'subject'), 'utf-8')

        smtp.connect(cf.getOneOptions('Email', 'sever_name'), port=25)
        smtp.login(user=cf.getOneOptions('Email', 'username'), password=cf.getOneOptions('Email', 'password'))

        smtp.sendmail(message['From'], message['To'].split(','), message.as_string())
        smtp.quit()
        myLogger.logger.info('Send Email Success!')
    except Exception as msg:
        myLogger.logger.error(msg)


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    htmlFile = os.path.join(report_path, 'result_' + now + '.html')
    with open(htmlFile, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title="移动安全会议系统项目(自动化测试报告)",
                                description="接口自动化测试报告如下所示："
                                )
        # 需要执行的模块名称
        model_name = ['SoftwareServices']
        model_name_all = []
        runner.run(run_model_test_case(model_name_all))
        # runner.run(run_model_test_case(model_name))
    lastFile = get_last_report_file(report_path)
    # sendEmail(lastFile)
