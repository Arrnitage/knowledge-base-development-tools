from flask import Flask, render_template, Response, request, redirect, url_for
from .utils.form import *
from knowledge.knowledge import Knowledge
from common.fileutils import check_file_exist
import os

app = Flask(__name__)
base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('/index.html')


# TODO: Need Fix(privilege has two condition string)
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
    data = request.form.to_dict()
    if 'location' in data:
        location = data['location']
        del data['location']
    if 'k_name' in data:
        filename = data['k_name'] + ".ttp"
    file_path = os.path.sep.join([base, 'offensive', location, filename])
    for key, value in data.items():
        pass
    return redirect(url_for('/editor'))


@app.route('/check', methods=['POST'])
def check():
    location = request.form['location']
    filename = request.form['filename'] + ".ttp"
    file_path = os.path.sep.join([base, 'offensive', location, filename])
    if not check_file_exist(file_path):
        return Response(":) OK, You can use this file name")
    else:
        return Response(":( Already Exist, Please change the file name")


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
