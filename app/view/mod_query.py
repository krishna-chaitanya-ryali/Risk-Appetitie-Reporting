from flask import Blueprint, request

SqlQry = Blueprint("SqlQry", __name__)

QueryString = {

    1:{"Qstring":"SELECT * FROM EMP"},
    2:{"Qstring":"SELECT * FROM DEP"}
}