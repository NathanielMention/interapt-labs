from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.path.join('sqlite://', basedir,'dogapi.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),unique=True)
    breed = db.Column(db.String(80))
    sex = db.Column(db.String(1))

    def __init__(self, name, breed, sex):
        self.name = name
        self.breed = breed
        self.sex = sex

class DogSchema(ma.Schema):
    class Meta:
        fields = ('name', 'breed', 'sex')

dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)

@app.route('/dog', methods=["POST"])
def add_dog():
    name = request.json['name']
    breed = request.json['breed']
    sex = request.json['sex']

    new_dog = Dog(name, breed, sex)

    db.session.add(new_dog)
    db.session.commit()

    return jsonify(new_dog)

@app.route('/dog', methods=["GET"])
def get_dog():
    all_dogs = Dog.query.all()
    result = dogs_schema.dump(all_dogs)
    return jsonify(result)

@app.route('dog/<id>', methods=["GET"])
def dog_detail(id):
    dog = Dog.query.get(id)
    return dog_schema.jsonify(dog)

@app.route('dog/<id>', methods=["PUT"])
def dog_update(id):
    name = request.json['name']
    breed = request.json['breed']
    sex = request.json['sex']

    dog = Dog.query.get(id)
    dog.name = name
    dog.breed = breed
    dog.sex = sex

    db.session.commit()
    return dog_schema.jsonify(dog)

@app.route('dog/<id>', methods=['DELETE'])
def dog_delete(id):
    dog = Dog.query.get(id)
    db.session.delete(dog)
    db.session.commit()

    return dog_schema.jsonify(dog)

if __name__ == '__main__':
    app.run(debug=True)
