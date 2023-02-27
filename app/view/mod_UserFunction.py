import datetime
import cx_Oracle

from config import *
from app.view.mod_query import *
from flask import jsonify
from flask import render_template

from flask import request
from flask import Blueprint
from flask import session
from app.view.log import logger_debug, logger_error, logger_audit, logger_msg, logger_acc

log_error = logger_error()
log_debug = logger_debug()
log_audit = logger_audit()
log_msg = logger_msg()
log_aud = logger_audit()
log_acc = logger_acc()

userfunction = Blueprint("userfunction", __name__)


class rapdb():
    def __init__(self):


        self.__con = cx_Oracle.connect(user=conf_userName, password=conf_password, dsn=self.dsn_tns,
                                       encoding="UTF-8", nencoding="UTF-8")
        self.__cursor = self.__con.cursor()

    def get_data(self, SqlQry, parm):
        try:
            l_cur = self.__cursor.var(cx_Oracle.CURSOR)
            self.__cursor.execute(SqlQry, parm)
            return self.__cursor
        except cx_Oracle.DataError as e:
            log_error.error("Error | mod_userfunction | get_data Cls" + str(e))

def sql_getData(a, b=[], qryOption=''):
    try:
        SqlQry = QueryString[a]['Qstring'] + qryOption
        Db_Con = rapdb()

        print("-inside sql_get data")
        print(SqlQry)

        allrecs = Db_Con.get_data(SqlQry, b)
        print(allrecs)
        colname = [desc[0] for desc in allrecs.description]

        vResult = []

        if not allrecs is None:
            for row in allrecs:
                vRecs = {}
                for i in range(len(colname)):
                    vRecs.update({colname[i]:row[i]})
                vResult.append(vRecs)

        Db_Con.endconnection()
        return  vResult

    except Exception as e:
        print("sql_getdata")
        print(e)
        return -1
