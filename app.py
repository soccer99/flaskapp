from config.settings import *

from apps.hardware.models import Hardware

from urls import *

print("Debug from app.py: " + str(DEBUG))

if __name__ == "__main__":
	db.create_all()
	if DEBUG == "True":
		app.run('0.0.0.0', debug=True)
	else:
		app.run('0.0.0.0', debug=False)