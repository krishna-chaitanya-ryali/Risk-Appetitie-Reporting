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
        self.dsn_tns = cx_Oracle.makedsn(conf_hostName, conf_port, service_name=conf_serviceName)
