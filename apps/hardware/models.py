from flask_migrate import Migrate

from config.settings import app, db



migrate = Migrate(app, db)

class Hardware(db.Model):
	id = db.Column('hardware_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	sn = db.Column(db.String(50))  
	company = db.Column(db.String(100))
	model = db.Column(db.String(60))
	
	def __init__(self, name, company, model, sn):
		self.name = name
		self.sn = sn
		self.company = company
		self.model = model
	
	def __repr__(self):
		return '<User %r>' % self.name