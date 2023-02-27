import cx_Oracle
from flask import Flask

cx_Oracle.init_oracle_client('')

app = Flask(__name__, static_folder ='static')
app.config.from_object('config.ProductionConfig')

#for refreshing css & js files, to be removed in live

app.config['SEND_FILE_MAX_AGE_DEFAULT']=1
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.view.mod_query import SqlQry
from app.view.mod_views import views
from app.view.mod_UserFunction import userfunction
from app.view.mod_footnote import footnote

app.register_blueprint(views)
app.register_blueprint(SqlQry)
app.register_blueprint(userfunction)
app.register_blueprint(footnote)
