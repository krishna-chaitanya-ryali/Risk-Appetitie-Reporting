import os
from datetime import timedelta

#Database Information
conf_userName = 'sys'
conf_password = 'Welcome_123'
conf_hostName = 'localhost'
conf_serviceName = 'orcl'
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