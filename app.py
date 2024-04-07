from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Gbook"
mongo = PyMongo(app)

@app.route('/insert_data', methods=['POST'])
def insert_data():
    username = request.form['username']
    print(username,flush=True)
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']

    if password != confirm_password:
        return jsonify({"message": "Passwords do not match"})

    collection = mongo.db.users  
    result = collection.insert_one({"username": username, "email": email, "password": password})

    return redirect('/main') 


@app.route('/')
def mainPage():
    return render_template('register.html')


cylinders = [
    {'name': 'Oxygen Cylinder', 'image': 'img/cylinder1.jpg', 'price': 100, 'capacity': '10L'},
    {'name': 'Nitrogen Cylinder', 'image': 'img/cylinder2.jpg', 'price': 150, 'capacity': '15L'},
    {'name': 'Medical Gas Cylinder', 'image': 'img/cylinder3.jpg', 'price': 80, 'capacity': '5L'},
    {'name': 'Helium Cylinder', 'image': 'img/cylinder4.jpg', 'price': 160, 'capacity': '15L'},
    {'name': 'Oygen Cylinder Pro', 'image': 'img/cylinder5.jpg', 'price': 190, 'capacity': '18L'},
    {'name': 'Medical Gas Cylinder', 'image': 'img/cylinder6.jpg', 'price': 60, 'capacity': '3L'},
    {'name': 'Propane Cylinder', 'image': 'img/cylinder7.jpg', 'price': 90, 'capacity': '8L'},
    {'name': 'Nitrogen Cylinder', 'image': 'img/cylinder8.jpg', 'price': 230, 'capacity': '20L'},
    {'name': 'Acetylene Gas Cylinder', 'image': 'img/cylinder9.jpg', 'price': 180, 'capacity': '15L'}
]


@app.route('/main')
def main():
    return render_template('mainPage.html', cylinders=cylinders)


if __name__ == '__main__':
    app.run(debug=True)
