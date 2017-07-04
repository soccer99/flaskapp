from config.settings import *

from apps.hardware.models import Hardware

from urls import *

if __name__ == "__main__":
	db.create_all()
	if DEBUG:
		app.run(debug=True)
	else:
		app.run(host='0.0.0.0')