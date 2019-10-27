import os
import requests, json
from app.models import User, Location
from app import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

some_engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=some_engine)
session = Session() 


class Helpers:

    @staticmethod
    def clear_data():

        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print ('Clear table %s' % table)
            session.execute(table.delete())
        session.commit()

    @staticmethod
    def get_data(app):
        with app.app_context(): 
            print("Populating users and addresses into database..")
            data = requests.get('https://randomuser.me/api/?results=100').text
            data = json.loads(data)
            results = data['results']
            store_list = []

            for item in results:
                title = item['name']['title']
                first = item['name']['first']
                last = item['name']['first']
                gender = item['gender']
                dob = item['dob']['date']
                phone = item['phone']
                cell = item['cell']
                nat = item['nat']
                email = item['email']
                username = item['login']['username']
                password = item['login']['password']
                thumbnail = item['picture']['thumbnail']
                user_info = [title, first, last, gender, dob, phone, cell, nat, email, username, password, thumbnail ]
                user = User(user_info)
                session.add(user)
                session.commit()
                session.flush()
               
                user_id = user.id
                street_number = item['location']['street']['number']
                street_name = item['location']['street']['name']
                city = item['location']['city']
                state = item['location']['state']
                country = item['location']['country']
                postcode = item['location']['postcode']
                latitude = item['location']['coordinates']['latitude']
                longitude = item['location']['coordinates']['longitude']
                timezone_offset = item['location']['timezone']['offset']
                timezone_description = item['location']['timezone']['description']
                location_info = [user_id, street_number, street_name, city, state, country, postcode, latitude, longitude, timezone_offset, timezone_description]
                location = Location(location_info)
                location.save()