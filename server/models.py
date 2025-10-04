from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.model, SerializerMixin):
	__tablename__ = 'earthquakes'
	
	id = db.Column(db.Integer, primary_key=True)
	magnitude = db.Column(db.Float, nullable=False)
	location = db.Column(db.String(100), nullable=False)
	year = db.Column(db.Integer, nullable=False)
	deaths = db.Column(db.Integer, nullable=True)
	
	def __repr__(self):
		return f'<Earthquake {self.id} - Magnitude: {self.magnitude}, Location: {self.location}>'
