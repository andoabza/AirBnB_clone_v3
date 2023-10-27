#!/usr/bin/python3

from flask import Flask
from models inport storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear():
    storage.close()

if __name__ == "__main__":
    if HBNB_API_HOST and HBNB_API_PORT:
        app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
    app.run(host=0.0.0.0, port=5000, threaded=True)

