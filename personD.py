from google.appengine.ext import ndb

class PersonD(ndb.Model):

     email_address = ndb.StringProperty()

     Anagram_Count = ndb.IntegerProperty()
     WordCount = ndb.IntegerProperty()

