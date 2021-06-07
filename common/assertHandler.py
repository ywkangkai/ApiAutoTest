import unittest


# 用于断言response body中反馈的json字符串
class AssertHandler(unittest.TestCase):
    def setUp(self):
        pass

    # 断言response_text中的result,message中的键值resultValue, messageValue
    # response_text表示返回的body
    # result,message表示断言的body的键
    # resultValue, messageValue表示断言的body对应键的键值
    def assert_body(self, response_text, result, message, result_value, message_value):
        for key in response_text:
            if key == result:
                self.assertEqual(response_text[key], result_value)
            if key == message:
                self.assertEqual(response_text[key], message_value)

    def tearDown(self):
        pass