from flask import Flask, redirect, url_for, request
from flask import render_template
from flask import session


app = Flask(__name__)
app.secret_key = '12345'

@app.route('/logout')
def logout():
    session['username'] = ''
    return render_template('home.html')


@app.route('/assignment9', methods=['GET', 'POST'])
def assig9():

    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']
            found = True
            if found:
                session['name'] = name
            if name == '':
                return render_template('assignment9.html',
                                       users={'user1': {'name': 'shahar', 'email': 'shahar@gmail.com'},
                                              'user2': {'name': 'yossi', 'email': 'yossi@gmail.com'},
                                              'user3': {'name': 'mor', 'email': 'mor@gmail.com'},
                                              'user4': {'name': 'tal', 'email': 'tal@gmail.com'},
                                              'user5': {'name': 'bar', 'email': 'bar@gmail.com'},
                                              'user6': {'name': 'ron', 'email': 'roni@gmail.com'}})
            else:
                return render_template('assignment9.html', name=name,
                                       users={'user1': {'name': 'shahar', 'email': 'shahar@gmail.com'},
                                              'user2': {'name': 'yossi', 'email': 'yossi@gmail.com'},
                                              'user3': {'name': 'mor', 'email': 'mor@gmail.com'},
                                              'user4': {'name': 'tal', 'email': 'tal@gmail.com'},
                                              'user5': {'name': 'bar', 'email': 'bar@gmail.com'},
                                              'user6': {'name': 'ron', 'email': 'roni@gmail.com'}})

        else:
            return render_template('assignment9.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        found = True
        if found:
            session['username'] = username
            return render_template('home.html', name=username)
        else:
            return render_template('assignment9.html')

    return render_template('assignment9.html')


@app.route('/assignment8')
def assig8():
    found = True
    if found:
        return render_template('assignment8.html',
                               profile={'name': 'shahar', 'last_name': 'vazana'},
                               university='BGU',
                               degrees=['B.A'],
                               hobbies=('play guitar', 'sing', 'run', 'hiking', 'music', 'sql'))
    else:
        return render_template('assignment8.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


@app.route('/home')
@app.route('/')
def home():
    found = True
    if found:
        return render_template('home.html', name='shahar')
    else:
        return render_template('home.html')


@app.route('/more')
def CV():
    return render_template('CVPage.html')


if __name__ == '__main__':
    app.run(debug=True)
