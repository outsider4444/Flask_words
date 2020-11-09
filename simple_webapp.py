from flask import Flask, session

from checker import check_logged_in

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'


@app.route('/login')
def do_login():
    session['logged_in'] = True
    return 'You are now logged in'


app.secret_key = 'YouWillNeverGuessMySecretKey'


@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/status')
def check_status():
    if 'logged_in' in session:
        return 'You are currently logged in'
    return 'You are not logged in'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This page 1.'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This page 2.'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'This page 3.'


if __name__ == '__main__':
    app.run(debug=True)
