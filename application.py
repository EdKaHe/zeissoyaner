from flask import Flask, Response
import os.path
import logging

logger = logging.getLogger('spam_application')
logger.info("test stuff")

app = Flask(__name__)

def get_file(filename):
    try:
        src = os.getcwd() + r"/" + filename
        return open(src).read()
    except IOError as exc:
        return str(exc)

#Main page
@app.route("/")
def mainSite():
    logging.info("executing main page")
    content = get_file("/templates/index.html")
    return Response(content, mimetype="text/html")

#test subpage
@app.route("/dash")
def dashboard():
    logging.info("executing test page")
    content = get_file("/templates/dash.html")
    return Response(content, mimetype="text/html")

if __name__ == "__main__":
    app.run()