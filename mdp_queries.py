from google.appengine.ext import ndb


DEFAULT_FILM_KEY = "film_key"


def film_key(film_name=DEFAULT_FILM_KEY):

    return ndb.Key('Film', film_name)


class Film(ndb.Model):

    name = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


def insert_into_entity_film():
    film = Film(parent=film_key("test_key"))

    film.name = "Film1"
    film.put()
