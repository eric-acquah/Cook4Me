#!/usr/bin/python3

"""
App entry point. Mainly used for testing classes

"""

from api.v1.app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


if __name__ == '__main__':
    app.run(debug=True)

