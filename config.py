import os
from datetime import timedelta

#Database Information
conf_userName = ''
conf_password = ''
conf_hostName = ''
conf_serviceName = ''
conf_port = ''
conf_dialect = ''
conf_sqldriver = ''

#user paths

class ProductionConfig():
    """Set app config vars."""
    SECRET_KEY = os.urandom(24)
    SESSION_TYPE = None
    SESSION_COOKIE_NAME = 'RAP_Session'
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = timedelta(1,5, 41038)