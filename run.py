import os
from app import create_app
from app.helpers import Helpers

app = create_app(os.getenv('APP_SETTINGS'))


Helpers.clear_data()
Helpers.get_data(app)

if __name__ == '__main__':
    app.run()
