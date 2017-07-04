from config.settings import *

from apps.hardware.models import Hardware

from urls import *

if __name__ == "__main__":
	db.create_all()
	app.run(debug = True)