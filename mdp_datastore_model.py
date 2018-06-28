import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2


import cgi

from google.appengine.datastore.datastore_query import Cursor
from google.appengine.ext import ndb
import webapp2


class Film(ndb.Model):
    """Models an individual Guestbook entry with content and date."""
    content = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_book(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.date)


class MainPage(webapp2.RequestHandler):
    MOVIES_PER_PAGE = 20

    def get(self):
        film_name = self.request.get('guestbook_name')
        ancestor_key = ndb.Key('Book', film_name or '*notitle*')
        films = Film.query_book(ancestor_key).fetch(
            self.MOVIES_PER_PAGE)

        self.response.out.write('<html><body>')

        for film in films:
            self.response.out.write(
                '<blockquote>%s</blockquote>' % cgi.escape(film.content))

        self.response.out.write('</body></html>')


class List(webapp2.RequestHandler):
    MOVIES_PER_PAGE = 10

    def get(self):
        """Handles requests like /list?cursor=1234567."""
        cursor = Cursor(urlsafe=self.request.get('cursor'))
        films, next_cursor, more = Film.query().fetch_page(
            self.MOVIES_PER_PAGE, start_cursor=cursor)

        self.response.out.write('<html><body>')

        for film in films:
            self.response.out.write(
                '<blockquote>%s</blockquote>' % cgi.escape(film.content))

        if more and next_cursor:
            self.response.out.write('<a href="/list?cursor=%s">More...</a>' %
                                    next_cursor.urlsafe())

        self.response.out.write('</body></html>')


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/list', List),
], debug=True)
