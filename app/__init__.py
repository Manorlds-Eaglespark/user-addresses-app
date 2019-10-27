import os
from flask_api import FlaskAPI
from flask import make_response, request, jsonify, abort, json
from flask_cors import CORS
from shared import db
from instance.config import app_config
from app.models import User, Location
from app.login_required import login_required

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    CORS(app)

    @app.route('/', methods=['GET'])
    def welcome_to_api():
        response = {"status": 200,
            "message": "Welcome To User Address API"}
        return make_response(jsonify(response)), 200

    @app.route('/api/v1/users', methods=['GET'])
    def fetch_all_users():
        users = User.get_all()
        results = []
        for user in users:
            obj = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "password": user.password,
            }
            results.append(obj)
        return make_response(jsonify({"results":results, "count": len(results)}))



    @app.route('/api/v1/user', methods=['GET'])
    @login_required
    def fetch_user_details(current_user):
        user = User.query.filter_by(id=current_user).first()
        user_data = {
            "title": user.title,
            "first": user.first,
            "last": user.last,
            "gender": user.gender,
            "dob": user.dob,
            "phone": user.phone,
            "cell": user.cell,
            "nat": user.nat,
            "email": user.email,
            "username": user.username,
            "password": user.password,
            "thumbnail": user.thumbnail
        }

        if user_data:
            location = Location.query.filter_by(user_id=user.id).first()
            location_data = {
                "address_id": location.id,
                "street_number": location.street_number,
                "street_name": location.street_name,
                "city" : location.city,
                "state": location.state,
                "country": location.country,
                "postcode": location.postcode,
                "latitude": location.latitude,
                "longitude": location.longitude,
                "timezone_offset": location.timezone_offset,
                "timezone_description": location.timezone_description
            }
        return make_response(jsonify({"status": 200, "user_data": user_data, "user_location": location_data})), 200


    @app.route('/api/v1/login', methods=['POST'])
    def login_user():
        e_mail = request.get_json().get('email','')
        password = request.get_json()['password']     
        user = User.query.filter_by(email=e_mail).first()
        if not e_mail or not password:
            return make_response(jsonify({"status": 400, "error": "Both Email and Password are required"})), 400
        if user:
            if password == user.password:
                access_token = User.generate_token(user.id)
                if access_token:
                    response = {
                                'status': 200,
                                'access_token': access_token,
                                'message': 'You successfully logged-in'
                            }
                    return make_response(jsonify(response)), 200
            else:
                return make_response(jsonify({"status": 403, "error": "Wrong Password entered"})), 403
        else:
            return make_response(jsonify({"status": 403, "error": "No user has that email in the database"})), 403

    @app.route('/api/v1/edit-address/<address_id>', methods=['PUT'])
    @login_required
    def update_user_address(current_user, address_id):
        address = Location.query.filter_by(id=address_id).first()
        if not address:
            return make_response(
                jsonify({"status": 404, "error": "Address not found."}))
        address.street_number = request.get_json().get('street_number','')
        address.street_name = request.get_json().get('street_name','')
        address.city = request.get_json().get('city','')
        address.state = request.get_json().get('state','')
        address.country = request.get_json().get('country','')
        address.postcode = request.get_json().get('postcode','')
        address.latitude = request.get_json().get('latitude','')
        address.longitude = request.get_json().get('longitude','')
        address.timezone_offset = request.get_json().get('timezone_offset','')
        address.timezone_description = request.get_json().get('timezone_description','')
        address.save()
        return make_response(jsonify({"status": 202, "message": "Successfully Updated Your Address!"})), 202
        


    return app
