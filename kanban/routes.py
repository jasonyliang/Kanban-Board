from flask import render_template, url_for, flash, redirect
from kanban import app

@app.route("/")
def home():
	return render_template('home.html')