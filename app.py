from flask import Flask, render_template

from app.views.organization import organization_blueprint
from app.views.user import user_blueprint
from database import init_db

app = Flask(__name__, template_folder="app/templates")
app.config.from_object('config')

app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(organization_blueprint, url_prefix="/organization")
init_db()


@app.route('/')
def hello_world():
    return render_template("login.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
