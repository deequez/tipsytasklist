
"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, request, redirect, session, g, url_for
import model

app = Flask(__name__)

@app.before_request
def set_up_db():
    g.db = model.connect_db()

@app.teardown_request
def disconnect_db(e):
    g.db.close()

@app.route("/")
def index():
    return render_template("index.html", user_name='chriszf')

@app.route("/tasks")
def list_tasks():
    if 'usr_id' in session:
        tasks_from_db = model.get_tasks(g.db, None)
        return render_template("list_tasks.html", tasks=tasks_from_db)
    return redirect(url_for("login"))

@app.route("/savetask", methods=["POST"])
def save_task():
    title = request.form['new_item']
    model.new_task(g.db, title, 1)
    return redirect(url_for("list_tasks"))

@app.route("/tasks/<int:id>", methods=["GET"])
def view_task(id):
    task_from_db = model.get_task(g.db, id)
    return render_template("view_tasks.html", task=task_from_db)

@app.route("/tasks/<int:id>", methods=["POST"])
def complete_task(id):
    model.complete_task(g.db, id)
    return redirect(url_for("list_tasks"))

@app.route("/login")
def login():
    return render_template("login.html"), redirect(url_for("list_tasks"))

@app.route("/authenticate", methods = ["POST"])
def authenticate():
    login_email = request.form['email']
    login_pw = request.form['password']
    usr_auth = model.authenticate(g.db, login_email, login_pw)
    session['usr_id'] = usr_auth['id']
    return redirect(url_for('list_tasks'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
        app.run(debug=True)