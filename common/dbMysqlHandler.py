import pymysql
import configHandler
import common.logHandler as myLogging
cf = configHandler.ConfigSetting()


class MySqlHandler:
    host = cf.getOneOptions("DB_OBJECT", "host")
    user = cf.getOneOptions("DB_OBJECT", "username")
    psw = cf.getOneOptions("DB_OBJECT", "password")
    port = cf.getOneOptions("DB_OBJECT", "port")
    database = cf.getOneOptions("DB_OBJECT", "sever_name")

    def __init__(self):
        global myLogger, db, cursor, dbConfig
        self.myLogger = myLogging.Logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        self.db = pymysql.connect(**dbConfig)
        self.cursor = self.db.cursor()
        self.myLogger.logger.info("DB connect success!")
        self.myLogger.logger.error("DB connect fail!")

    # 执行Sql文件
    def excute(self, sql, params):
        self.connectDB()
        self.cursor.excute(sql, params)
        self.db.commite()
        return self.cursor

    def get_all(self):
        value = self.cursor.fetchall()
        return value

    def get_one(self):
        value = self.cursor.fetchone()
        return value

    def close_db(self):
        self.db.close()
