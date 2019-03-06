from flask import render_template, url_for, flash, redirect
from kanban import app, db
from kanban.models import Todo
import os
from kanban.forms import ToDoForm
from sqlalchemy import and_, or_, not_



@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/", methods=['POST', 'GET'])
def home():
	todos = Todo.query.filter_by(do=False, done=False).all()
	dos = Todo.query.filter_by(do=True, done=False).all()
	dones = Todo.query.filter_by(do=True, done=True).all()
	return render_template('home.html', todos=todos, dos=dos, dones=dones)


@app.route("/add", methods=['POST', 'GET'])
def add_todo():
	form = ToDoForm()
	if form.validate_on_submit():
		todo = Todo(title=form.title.data, description=form.description.data, deadline=form.deadline.data)
		db.session.add(todo)
		db.session.commit()
		flash(f'Todo {form.title.data} created!', 'success')
		return redirect(url_for('home'))
	return render_template('add.html', form=form, title="Add Todo")