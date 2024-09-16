from flask import Flask
from controllers.post_controller import post_blueprint

app = Flask(__name__)
app.register_blueprint(post_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
