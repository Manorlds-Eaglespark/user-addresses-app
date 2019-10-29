# User-Addresses-App
Offer API access for users addresses

## GETTING STARTED
* Clone this repo using 

  ```git clone https://github.com/Manorlds-Eaglespark/user-addresses-app.git```

* Then change directory to the new folder
  
  ```cd <Directory-Name> ```

* Create a virtual environment
  
  ```virtualenv <virtual-env-name>```

* Activate the virtual environment

  ```. <virtual-env-name>/bin/activate```

* Switch to the appropriate branch and follow along.

## REQUIREMENTS

* Install all the dependencies in your virtual environment
  
  ```pip install -r requirements.txt```

## PREREQUITES
- A Working computer. Linnux, windows or Mac OS
- Postman, to test endpoints
- Git, to follow different repo branches smoothly.
- Text Editor, preferably Visual Studio Code.

# Heroku API Endpoints

| HTTP Method  | End Point       | Public Access      |  Action            |  Authentication  |
| :------------:|:---------------:| :---------------:|:---------------------:|:---------------------:|
| GET    | /api/v1/users | TRUE |  get users to login  | No   |
| POST    | /api/v1/login | TRUE |  Login a user from the above url  |  No  |
| GET    | /api/v1/user | TRUE |  Fetch a logged-in user details.  |  Yes |
| PUT    | /api/v1/edit-address/<address_id>        |  TRUE |   Edit a user's address    |  Yes |

## Built With
Python 3.6, Flask Micro-framework

## Tools Used
-Pylint
-Pytest
-Virtual environment

## Hosted API
Follow this [link](https://address-app-256.herokuapp.com/)

## Host UI Demo
This app has a UI mock in react - redux. Find it [here](https://github.com/Manorlds-Eaglespark/User-Address-App-FrontEnd)

## AUTHOR
[Anorld Mukone](https://github.com/Manorlds-Eaglespark)

