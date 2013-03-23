import sqlite3


def connect_db():
    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):
    c = db.cursor()
    query = """INSERT INTO users VALUES (NULL, ?, ?, ?)"""
    result = c.execute(query, (email, password, name))
    db.commit()
    return result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * FROM users WHERE email=? AND password=?""" 
    c.execute(query, (email, password))
    result = c.fetchone()

    if result:
        keys = ["id", "email", "password", "name"]
        return dict(zip(keys, result))

    return None

def new_task(db, title, user_id):
    c = db.cursor()
    query = """INSERT INTO tasks VALUES (NULL, ?, datetime(), NULL, ?)"""
    result = c.execute(query, (title, user_id))
    db.commit()
    return result.lastrowid

def get_user(db, user_id):
    c = db.cursor()
    query = """SELECT * FROM users WHERE id=?"""
    c.execute(query, (user_id))
    result = c.fetchone()

    if result:
        keys = ["id", "email", "password", "name"]
        return dict(zip(keys, result))

    return None 

def complete_task(db, task_id):
    c = db.cursor()
    query = """UPDATE tasks SET completed_at=datetime() WHERE id=?"""
    c.execute(query, (task_id, ))
    db.commit()

def get_tasks(db, user_id):
    c = db.cursor()
    query = """ SELECT * FROM tasks WHERE user_id=?"""
    c.execute(query, (user_id, ))
    result = c.fetchall()

    if result:
        user_tasks_list = []
        keys = ["id", "title", "created_at", "completed_at", "user_id"]
        
        for i in enumerate(result):
            user_tasks_list.append(dict(zip(keys, i[1])))
            return user_tasks_list
    
    else: 
        query = """SELECT * FROM tasks"""
        c.execute(query)
        result = c.fetchall()

        all_tasks_list = []        
        keys = ["id", "title", "created_at", "completed_at", "user_id"]

        for i in enumerate(result):
           all_tasks_list.append(dict(zip(keys, i[1]))) 
           return all_tasks_list

def get_task(db, task_id):
    c = db.cursor()
    query = """SELECT * FROM tasks WHERE id=?"""
    c.execute(query, (task_id, ))
    result = c.fetchone()

    if result:
        keys = ["id", "title", "created_at", "completed_at", "user_id"]
        return dict(zip(keys,result))

    return None 