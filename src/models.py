from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#user
#[GET] /users  //  [GET] /users/favorites
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    favorite_people = db.relationship('Favorite_People', backref='user', lazy=True)
    favorite_planets = db.relationship('Favorite_Planet', backref='user', lazy=True)

    def serialize(self):
        return {
        "id": self.id, 
        "username": self.username, 
        }
    
#PEOPLE_FAV
#[GET] /people  //  #[GET] /people/<int:people_id> // 
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
        "id": self.id, 
        "name": self.name, 
        "height": self.height, 
        "gender": self.gender, 
        "created": self.created, 
        "url": self.url
        }
        
#[POST] /favorite/people/<int:people_id> // #[DELETE] /favorite/people/<int:people_id>
class Favorite_People(db.Model):
    __tablename__ = 'favorites_peoples'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)

#PLANETS_FAV
#[GET] /planets // #[GET] /planets/<int:planet_id> // 
class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    population = db.Column(db.String, nullable=False)
    url = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
        "id": self.id, 
        "name": self.name, 
        "diameter": self.height, 
        "climate": self.gender, 
        "population": self.created, 
        "url": self.url
        }

#[POST] /favorite/planet/<int:planet_id> // #[DELETE] /favorite/planet/<int:planet_id>
class Favorite_Planet(db.Model):
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
