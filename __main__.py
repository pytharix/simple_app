from flask import Flask, render_template
import socket

apps = Flask(__name__, template_folder='assets')
apps.secret_key = 'TinyJar Production'
apps.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root@127.0.0.1/tiny_jar'
apps.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

host = socket.gethostbyname(socket.gethostname())


@apps.route('')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    apps.run(host=host, port=5000, debug=True)
