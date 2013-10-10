
from flask import Flask, request, redirect, url_for, render_template

app=Flask(__name__)

PASSWORD = "password"
USERNAME = "james"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['user'] == USERNAME:
            if request.form['password'] == PASSWORD:
                return redirect(url_for('hello'))
    return render_template('htmlExample.html')

@app.route('/hi')
def hello():
    return("Hello %s" % USERNAME)


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
