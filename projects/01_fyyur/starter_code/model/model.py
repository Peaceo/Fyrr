from app import db



class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False)
    city = db.Column(db.String(120), nullable= False)
    state = db.Column(db.String(120), nullable= False)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))
    Show = db.relationship('Show', backref="Venue", lazy=True)


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))

    Show = db.relationship('Show', backref="Artist", lazy=True)
# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.


class Show(db.Model):
      __tablename__ = 'Show'
      id = db.Column(db.Integer, primary_key=True)
      artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'),nullable=False)
      venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'),nullable=False)
      start_time = db.Column(db.String(50), nullable = False)
