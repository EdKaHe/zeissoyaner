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
def hello():
    logging.info("executing main page")
    return "Hello World!"

#test subpage
@app.route("/test")
def testpage():
    logging.info("executing test page")
    content = get_file("/Frontend/testfile.html")
    return Response(content, mimetype="text/html")

#test subpage2
@app.route("/test2")
def testpage2():
    logging.info("executing test page")
    content = get_file("/Frontend/testfile2.html")
    return Response(content, mimetype="text/html")


if __name__ == "__main__":
    app.run()

