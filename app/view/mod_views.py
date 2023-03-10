from app.view.mod_UserFunction import *
from flask import Blueprint, request

log_error = logger_error()
log_debug = logger_debug()
log_audit = logger_audit()
log_msg = logger_msg()
log_aud = logger_audit()
log_acc = logger_acc()

views = Blueprint("views", __name__)

@views.route("/", methods=["GET","POST"])
def news_announcement():
    try:
        new_text = get_news_data()
        return checkmyaccess("home.html")
    except Exception as e:
        log_error.error('Error | mod_views | generic home| ' +str(e))

