import os
import jwt
# from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
from app import db

class User(db.Model):
    """This class represents the user table."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    first = db.Column(db.String(255))
    last = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    dob = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    cell = db.Column(db.String(255))
    nat = db.Column(db.String(255))
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __init__(self, info_list):
        """initialize with user info."""
        self.title = info_list[0]
        self.first = info_list[1]
        self.last = info_list[2]
        self.gender = info_list[3]
        self.dob = info_list[4]
        self.phone = info_list[5]
        self.cell = info_list[6]
        self.nat = info_list[7]
        self.email = info_list[8]
        self.username = info_list[9]
        self.password = info_list[10]
        self.thumbnail = info_list[11]
        # self.password = Bcrypt().generate_password_hash(info_list[10]).decode() 
        # Did not use it to make it easier for you to login users.

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def password_is_valid(given_password, password):
        return Bcrypt().check_password_hash(password, given_password)

    @staticmethod
    def generate_token(user_id):
        """ Generates the access token"""
        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=15),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            # create the byte string token using the payload and the SECRET key
            jwt_string = jwt.encode(
                payload,
                str(os.getenv('SECRET')),
                algorithm='HS256'
            )
            return jwt_string.decode()

        except Exception as e:
            # return an error in string format if an exception occurs
            return str(e)

    @staticmethod
    def decode_token(token):
        """Decodes the access token from the Authorization header."""
        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, current_app.config.get('SECRET'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return "Invalid token. Please register or login"

    def user_json(self):
        return {
            "title": self.title,
            "first": self.first,
            "last": self.last,
            "gender": self.gender,
            "dob": self.dob,
            "phone": self.phone,
            "cell": self.cell,
            "nat": self.nat,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "thumbnail": self.thumbnail
        }


class Location(db.Model):
    """This class represents the location table."""

    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)           
    user_id = db.Column(db.Integer, nullable=False,)
    street_number = db.Column(db.String(255))
    street_name = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    country = db.Column(db.String(255))
    postcode = db.Column(db.Integer)
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    timezone_offset = db.Column(db.String(255))
    timezone_description = db.Column(db.String(255))
    

    def __init__(self, info_list):
        """initialize with user info."""
        self.user_id = info_list[0]
        self.street_number = info_list[1]
        self.street_name = info_list[2]
        self.city = info_list[3]
        self.state = info_list[4]
        self.country = info_list[5]
        self.postcode = info_list[6]
        self.latitude = info_list[7]
        self.longitude = info_list[8]
        self.timezone_offset = info_list[9]
        self.timezone_description = info_list[10]
      
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Location.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Location: {}>".format(self.city)
