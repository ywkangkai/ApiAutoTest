import cx_Oracle
import common.logHandler as myLogging
import configHandler


class DbOraConfig:
    def __init__(self):
        global db, cf, myLogger
        myLogger = myLogging.Logger()
        cf = configHandler.ConfigSetting()

    def dbConnet(self, dbAction):
        try:
            host = cf.getOneOptions(dbAction, 'host')
            user = cf.getOneOptions(dbAction, 'username')
            psw = cf.getOneOptions(dbAction, 'password')
            server = cf.getOneOptions(dbAction, 'sever_name')
            port = cf.getOneOptions(dbAction, 'port')
            tns = cx_Oracle.makedsn(str(host), int(port), server)
            self.db = cx_Oracle.connet(user, psw, tns)
            myLogger.logger.info('Sql connet successful!')
            return self.db
        except Exception as msg:
            myLogger.logger.error(msg)

    def executeSqlResult(self, dbAction, sql, argsDict):
        consor = self.dbConnet(dbAction).consor()
        try:
            res = consor.execute(sql, argsDict)
            myLogger.logger.info('Sql execute result%s' % res)
            return res
        except Exception as msg:
            myLogger.logger.error(msg)

    def dbClose(self):
        db.close()
