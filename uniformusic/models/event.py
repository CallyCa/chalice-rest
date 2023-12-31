from uniformusic.extensions import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    date = db.Column(db.Date, nullable=False)

    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))

    def __init__(self, **kwargs):
        super(Event, self).__init__(**kwargs)

    def __repr__(self):
        return "<Event {} - {} - {}>".format(self.date, self.description, self.song.name)
