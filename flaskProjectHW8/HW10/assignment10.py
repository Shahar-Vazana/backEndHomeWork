import mysql
import requests
import random
from flask import Flask, redirect, url_for, request, Blueprint, flash, jsonify
from flask import render_template
from flask import session
from flask import jsonify
from InteractWithDC import interact_db

# about blueprint definition
assignment10 = Blueprint('HW10',
                         __name__,
                         static_folder='/static',
                         static_url_path='/HW10',
                         template_folder='templates')


# Routes


@assignment10.route('/assigment11/outer_source', methods=['GET'])
def assignment11_func():
    if 'number' in request.args:
        number = request.args['number']
        req = requests.get(url=f"https://reqres.in/api/users/{number}")
        req = req.json()
        return render_template('assigment11_outer.html', user=req['data'])
    # user_id = request.args['number']
    return render_template('assigment11_outer.html')


# def get_pockemons(num=3):
#     pockemons = []
#     for i in range(num):
#         random_n = random.randint(1, 100)
#         res = requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{random_n}')
#         res = res.json()
#         pockemons.append(res)
#     return pockemons

# def get_users(x):
#     users = []
#     res = requests.get(f'https://reqres.in/api/users/{x}')
#     # res = requests.get('https://reqres.in/api/users/%s' % x)
#     res = res.json()
#     users.append(res)
#     return users
#
#
# @assignment10.route('/req_backend')
# def req_backend_func():
#     x = 3
#     if "number" in request.args:
#         x = int(request.args['number'])
#     users = get_users(x)
#     return render_template('req_backend.html', users=users)
#

@assignment10.route('/assignment11/users')
def get_users_func():
    return_dict = {}
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    for user in users:
        return_dict[f'user_{user.id}'] = {
            'status': 'success',
            'name': user.name,
            'email': user.email,
        }
    return jsonify(return_dict)


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



# query = "select * from users"
# userss = interact_db(query=query, query_type='fetch')
# users_dict = {}
# users_array = [len(users)]
# # if len(users) == 0:
# #     return_dict = {
# #         'status': 'failed',
# #         'message': 'user not found'
# #     }
# # else:
# for u in users:
#     users_array[u] = '1'
#     # users_array[u] = users_dict.update({
#     #     'id': users[u].id,
#     #     'name': users[u].name,
#     #     'email': users[u].email})
#
# return jsonify(users_array)


# @assignment10.route('/users')
# def users_func():
#     query = 'select * from users;'
#     users = interact_db(query=query, query_type='fetch')
#     return f'{users}'


#
# def connector(query, query_type: str):
#     return_value = False
#     db = mysql.connector.connect(host="localhost",
#                                  user="root",
#                                  passwd="root",
#                                  database="web_database")
#
#     cursor = db.cursor(named_tuple=True)
#     cursor.execute(query)
#
#     if query_type == 'commit':
#         db.commit()
#         return_value = True
#     if query_type == 'fetch':
#         query_result = cursor.fetchall()
#         return_value = query_result
#     db.close()
#     cursor.close()
#     return return_value
#
#
# @assignment10.route("/assignment11/users", methods=["GET"])
# def users():
#     # if request.method == 'GET':
#     result = connector("SELECT * FROM users", query_type="fetch")
#     if len(result) == 0:
#         return jsonify({
#             'success': 'False: User not found',
#             "data": []
#         })
#     else:
#         return jsonify({
#             'success': 'True: User found',
#             "data": result
#         })
#

# @assignment10.route('/db_users', defaults={'user_id': -1, 'orders': 'my orders'})
# @assignment10.route('/db_users/<int:user_id>', defaults={'orders': 'my orders'})
# @assignment10.route('/db_users/<int:user_id>/<orders>')
# def get_users_func(user_id, orders):
#     if user_id == -1:
#         return_dict = {}
#         query = 'select * from users;'
#         users = interact_db(query=query, query_type='fetch')
#         for user in users:
#             return_dict[f'user_{user.id}'] = {
#                 'status': 'success',
#                 'name': user.name,
#                 'email': user.email,
#             }
#     else:
#         query = 'select * from users where id=%s;' % user_id
#         users = interact_db(query=query, query_type='fetch')
#         # print(type(user_id))
#         if len(users) == 0:
#             return_dict = {
#                 'status': 'failed',
#                 'message': 'user not found'
#             }
#         else:
#             return_dict = {
#                 'status': 'success',
#                 'id': users[0].id,
#                 'name': users[0].name,
#                 'email': users[0].email,
#                 'orders': orders,
#             }
#     return jsonify(return_dict)
#
