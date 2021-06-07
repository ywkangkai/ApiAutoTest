import logging
import os
from logging import handlers


class Logger(object):
    # 定义日志等级
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warn': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    filepath = os.path.join(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))),
        'log/autotest.log')

    def __init__(self, filename=filepath, level='info', when='D', backupCount=3,
                 fmt='%(asctime)s-%(pathname)s-%(lineno)d-%(levelname)s-%(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        if not self.logger.handlers:
            th = logging.handlers.TimedRotatingFileHandler(
                filename=filename, when=when, backupCount=backupCount, encoding='utf=8')
            th.setFormatter(format_str)
            self.logger.addHandler(th)
            sh = logging.StreamHandler()
            sh.setFormatter(format_str)
            self.logger.addHandler(sh)


if __name__ == '__main__':
    pass
