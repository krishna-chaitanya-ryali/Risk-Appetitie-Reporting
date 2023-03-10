import os
from datetime import timedelta

#Database Information
conf_userName = 'system'
conf_password = 'system'
conf_hostName = 'localhost'
conf_serviceName = 'orclpdb'
conf_port = '1521'
conf_dialect = 'oracle'
conf_sqldriver = 'cx_oracle'

#user paths

class ProductionConfig():
    """Set app config vars."""
    SECRET_KEY = os.urandom(24)
    SESSION_TYPE = None
    SESSION_COOKIE_NAME = 'RAP_Session'
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = timedelta(1,5, 41038)