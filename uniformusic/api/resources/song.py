from flask_jwt_extended import jwt_required
from flask_marshmallow import fields
from flask_restful import Resource

from uniformusic.commons.pagination import paginate
from uniformusic.extensions import ma, db
from uniformusic.models.song import Song
from marshmallow import Schema

class SongSchema(Schema):
    name = fields.fields.Str()
    spotify_id = fields.fields.Str()

    artist = ma.Nested('ArtistSchema', exclude=('songs', 'events'))
    events = ma.Nested('EventSchema', many=True, exclude=('song', 'artist'))

    class Meta:
        model = Song
        sqla_session = db.session


class SongResource(Resource):
    method_decorators = [jwt_required]

    def get(self, song_id):
        schema = SongSchema()
        song = Song.query.get_or_404(song_id)
        return {"song": schema.dump(song).data}


class SongList(Resource):
    method_decorators = [jwt_required]

    def get(self):
        schema = SongSchema(many=True)
        query = Song.query
        return paginate(query, schema)
