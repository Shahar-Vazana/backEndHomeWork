from flask import Flask, redirect, url_for, request, Blueprint, flash
from flask import render_template
from flask import session
from InteractWithDC import interact_db

# about blueprint definition
assignment10 = Blueprint('HW10',
                         __name__,
                         static_folder='/static',
                         static_url_path='/HW10',
                         template_folder='templates')


# Routes
@assignment10.route('/assignment10')
def index():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/UpdateuserName', methods=['GET', 'POST'])
def nameuserupdate():
    if request.method == 'POST':
        user_id = request.form['id']
        name = request.form['name']
        query = "UPDATE users SET name='%s' WHERE id='%s' ;" % (name, user_id)
        interact_db(query=query, query_type='commit')
        flash(f' user {user_id} updated!', 'success')
        return redirect('/assignment10')
    return redirect('/assignment10')


@assignment10.route('/UpdateuserEmail', methods=['GET', 'POST'])
def emailuserupdate():
    if request.method == 'POST':
        user_id = request.form['id']
        email = request.form['email']
        query = "UPDATE users SET email='%s' WHERE id='%s' ;" % (email, user_id)
        interact_db(query=query, query_type='commit')
        flash(f' user {user_id} updated!', 'success')
        return redirect('/assignment10')
    return redirect('/assignment10')


@assignment10.route('/deleteusers', methods=['GET', 'POST'])
def usersdelete():
    if request.method == 'GET':
        user_id = request.args['id']
        query = "DELETE FROM users WHERE id='%s';" % user_id
        interact_db(query, query_type='commit')
        flash(f' user {user_id} deleted!', 'success')
        return redirect('/assignment10')
    return redirect('/assignment10')


# @app.route('/deleteusers')
# def usersdelete():
#     userId = request.form['id']
#     query = "DELETE FROM users WHERE id='%s';" % userId
#     interact_db(query=query, query_type='commit')
#     return redirect('/assignment10')


@assignment10.route('/Insertuser', methods=['POST'])
def usersInsert():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    query = "INSERT INTO users(name, email, password) VALUES ('%s','%s','%s')" % (name, email, password)
    interact_db(query=query, query_type='commit')
    flash(f' user added!', 'success')
    return redirect('/assignment10')


# @assignment10.route('/users')
# def users():
#     query = "select * from users"
#     query_result = interact_db(query=query, query_type='fetch')
#     return render_template('assignment10.html', users=query_result)
