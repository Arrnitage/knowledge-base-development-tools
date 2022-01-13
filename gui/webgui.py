from flask import Flask, render_template, redirect, url_for, Response
from .utils.form import *
from knowledge.knowledge import Knowledge
from common.fileutils import check_file_exist

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
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


# TODO save offensive tech file via post request
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


# TODO view an offensive tech file via get request
@app.route('/view/{directory}/{file}', methods=['GET'])
def view(directory, file):
    return render_template('/view.html',
                           directory=directory,
                           file=file
                           )


# TODO open an offensive tech file edit page via get request
@app.route('/edit/{directory}/{file}', methods=['GET'])
def edit(directory, file):
    return render_template('/edit.html',
                           directory=directory,
                           file=file
                           )


# TODO delete interface via post request
@app.route('/delete', methods=['POST'])
def delete(directory, file):
    return Response("SUCCESS")
