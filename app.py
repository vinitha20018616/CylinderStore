from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/CylinderStore"
mongo = PyMongo(app)


@app.route('/')
def mainPage():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
