from config.settings import app, db


class Hardware(db.Model):
	id = db.Column('hardware_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	sn = db.Column(db.String(100))  
	company = db.Column(db.String(200))
	model = db.Column(db.String(10))
	
	def __init__(self, name, company, model, sn):
		self.name = name
		self.sn = sn
		self.company = company
		self.model = model
	
	def __repr__(self):
		return '<User %r>' % self.name