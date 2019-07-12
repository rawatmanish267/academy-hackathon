import os

from flask import Flask
from flask import request
from flask import render_template
todo_store={}
todo_store['raj']=['play','dance']
todo_store['shivang']=['study']
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that list my todos
    def insert_todos(name,todo):
        global todo_store
        todo_store[name].append(todo)
        return
    def add_todo_by_name(name,todo):
        insert_todos(name,todo)
        return
    def select_todo(name):
        global todo_store
        return todo_store[name]
    def get_todo_by_name(name):
        try:
           return select_todo(name)
        except:
            return None
    @app.route('/todo')
    def todos():
        name=request.args.get('name')
        print (name)
        todo_person=get_todo_by_name(name)
        if todo_person==None:
            return render_template('404.html'),404
        else:
            return render_template('myview.html',todos=todo_person)
    @app.route('/add_todo')
    def add_todos():
        name=request.args.get('name')
        todo=request.args.get('todo')
        print (name,todo)
        add_todo_by_name(name,todo)
        return "added sucessfully"
    return app

