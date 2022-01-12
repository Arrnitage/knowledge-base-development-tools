from flask import Flask, render_template, redirect, url_for, Response
from .utils.form import *
from knowledge.knowledge import Knowledge
from common.fileutils import check_file_exist

app = Flask(__name__)


@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')


@app.route('/editor', methods=['GET', 'POST'])
def editor():
    return render_template('/editor.html',
                           procedure=procedure(),
                           host_a=host("a"),
                           host_b=host("b"),
                           exports=export()
                           )


# TODO
@app.route('/submit', methods=['POST'])
def submit():
    # return Response("SUCCESS")
    file_path = ""
    items = dict()
    try:
        k = Knowledge()
        k.write(file_path)
        return Response("SUCCESS")
    except Exception as e:
        return Response(str(e))


@app.route('/check', methods=['POST'])
def check():
    file_path = ""
    if check_file_exist(file_path):
        return Response("SUCCESS")
    else:
        return Response("BAD")
