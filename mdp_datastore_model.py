import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

import mdp_queries

import cgi

from google.appengine.datastore.datastore_query import Cursor
from google.appengine.ext import ndb
import webapp2

DEFAULT_FILM_KEY = "film_key"

def film_key(film_name=DEFAULT_FILM_KEY):
    """Constructs a Datastore key for a Guestbook entity.

    We use guestbook_name as the key.
    """
    return ndb.Key('Film', film_name)



class MainPage(webapp2.RequestHandler):
    MOVIES_PER_PAGE = 20

    mdp_queries.insert_into_entity_film()

    def get(self):

        self.response.out.write('<html><body>')


        self.response.out.write('</body></html>')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
