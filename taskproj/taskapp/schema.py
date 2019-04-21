import graphene  
from graphene_django.types import DjangoObjectType, ObjectType  
from models import Song, artist, Album

class SongType(DjangoObjectType):  
    class Meta:
        model = Song

class artistType(DjangoObjectType):  
    class Meta:
        model = artist

class AlbumType(DjangoObjectType):  
    class Meta:
        model = Album

class Query(ObjectType):  
    songs = graphene.List(SongType)
    artists= graphene.List(artistType)
    Albums= graphene.List(AlbumType)

    def resolve_songs(self, info, **kwargs):
        return Song.objects.all()

    def resolve_artists(self, info, **kwargs):
        return artist.objects.all()

    def resolve_albums(self, info, **kwargs):
        return Album.objects.all()

schema = graphene.Schema(query=Query)
