# !/Users/mackmerriman/cos333/A4-cos333/reg.py

# Author: Mack Merriman
#-----------------------------------------------------------------------

import flask
from queryprep import query_prep
from dbaccess import db_access
from detailsdbdisplay import details_db_display

app = flask.Flask(__name__, template_folder=".")

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():

    html_code = flask.render_template("index.html")
    response = flask.make_response(html_code)
    return response

@app.route("/classresults", methods=["GET"])
def classresults():

    prev_search = ["","","",""]
    prev_search[0] = flask.request.args.get("dept")
    prev_search[1] = flask.request.args.get("num")
    prev_search[2] = flask.request.args.get("area")
    prev_search[3] = flask.request.args.get("title")

    for i in range(0, len(prev_search), 1):
        if prev_search[i] is None:
            prev_search[i] = ""

    statement = query_prep(prev_search)
    table, fail = db_access(statement)

    if fail:
        html_code = flask.render_template("error.html")
        response = flask.make_response(html_code)
        return response

    html_code = flask.render_template("classes.html",
                                      table=table)
    response = flask.make_response(html_code)
    return response

@app.route("/details", methods=["GET"])
def details():

    titles = ["Course Id:", "Days:", "Start time:",
              "End time:", "Building:", "Room:"]
    titles2 = ["Area:", "Title:", "Description:",
              "Prerequisites:"]

    classid = flask.request.args.get('classid')

    if not classid:
        html_code = flask.render_template("missing_error.html")
        response = flask.make_response(html_code)
        return response

    if not classid.isdigit():
        html_code = flask.render_template("classid_type_error.html")
        response = flask.make_response(html_code)
        return response

    tables, fail = details_db_display(classid)

    if fail == 2:
        html_code = flask.render_template("classid_error.html",
                                      classid=classid)
        response = flask.make_response(html_code)
        return response

    if fail == 1:
        html_code = flask.render_template("error.html")
        response = flask.make_response(html_code)
        return response

    classnum = tables[0]
    specs = tables[1]
    coursenum = tables[2]
    cross = tables[3]
    info = tables[4]
    profs = tables[5]


    html_code = flask.render_template("details.html",
                                      classnum=classnum,
                                      specs=specs,
                                      coursenum=coursenum,
                                      cross=cross,
                                      info=info,
                                      profs=profs,
                                      titles=titles,
                                      titles2=titles2)
    response = flask.make_response(html_code)
    return response
