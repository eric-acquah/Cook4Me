"""
This is the main entry point for the flask app

"""

from api.v1.resources import app_bp
from flask import Flask

app = Flask(__name__)


app.register_blueprint(app_bp)


# if __name__ == '__main__':
#     app.run(debug=True)