from flask import render_template, url_for, flash, redirect
from kanban import app, db, bcrypt
from kanban.models import Todo, User
import os
from kanban.forms import ToDoForm, RegistrationForm, LoginForm
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

@app.route("/do/<int:todo_id>")
def do(todo_id):
	todo = Todo.query.get_or_404(todo_id)
	todo.do = True
	todo.done = False
	db.session.commit()
	flash(f"The Todo '{todo.title}' has been moved to 'Do'!", "success")
	return redirect(url_for('home'))

@app.route("/done/<int:todo_id>")
def done(todo_id):
	todo = Todo.query.get_or_404(todo_id)
	todo.do = True
	todo.done = True
	db.session.commit()
	flash(f"The Todo '{todo.title}' has been moved to 'Done'!", "success")
	return redirect(url_for('home'))

@app.route("/todo/<int:todo_id>")
def todo(todo_id):
	todo = Todo.query.get_or_404(todo_id)
	todo.do = False
	todo.done = False
	db.session.commit()
	flash(f"The Todo '{todo.title}' has been moved to 'ToDo'!", "success")
	return redirect(url_for('home'))

@app.route("/items/<int:todo_id>")
def items(todo_id):
	todo = Todo.query.get_or_404(todo_id)
	return render_template('items.html', todo=todo, title=f"Todo Item: {todo.title}")

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
	todo = Todo.query.get_or_404(todo_id)
	db.session.delete(todo)
	db.session.commit()
	flash("Todo Removed!", "danger")
	return redirect(url_for('home'))



# users 
@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# generate hashed password
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title="Register", form=form)

