from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


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
